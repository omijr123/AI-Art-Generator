import time
import logging
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import errno
import traceback

logger = logging.getLogger(__name__)

class VideoGenerator:
    def __init__(self):
        self.model_loaded = False
        self.image_generator = None
    
    def safe_create_directory(self, directory_path):
        """Safely create directory without Windows errors"""
        try:
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                logger.warning(f"Directory creation issue: {e}")
    
    def create_fallback_video(self, prompt, style, output_path, duration=4):
        """Create a fallback video when AI fails"""
        try:
            width, height = 512, 512
            fps = 8
            total_frames = int(duration * fps)
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            for i in range(total_frames):
                # Create frame with error message
                frame = np.zeros((height, width, 3), dtype=np.uint8)
                frame[:, :] = [53, 53, 53]  # Dark gray background
                
                # Convert to PIL for text
                pil_img = Image.fromarray(frame)
                draw = ImageDraw.Draw(pil_img)
                
                # Try to load font
                try:
                    font = ImageFont.truetype("arial.ttf", 20)
                except:
                    font = ImageFont.load_default()
                
                # Draw error message
                lines = [
                    "🎥 AI Video Generation Failed",
                    f'Prompt: "{prompt}"',
                    f"Style: {style}",
                    f"Frame {i+1}/{total_frames}",
                    "",
                    "AI models are currently",
                    "being optimized..."
                ]
                
                y = 100
                for line in lines:
                    bbox = draw.textbbox((0, 0), line, font=font)
                    text_width = bbox[2] - bbox[0]
                    x = (width - text_width) // 2
                    draw.text((x, y), line, fill=(255, 255, 255), font=font)
                    y += 40
                
                # Convert back to OpenCV format
                frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
                video_writer.write(frame)
            
            video_writer.release()
            logger.info(f"✅ Fallback video created: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Fallback video creation failed: {e}")
            return False
    
    def generate(self, prompt, style="realistic", duration=4, enhance_prompt=False, output_path="output.mp4"):
        """Generate video from text prompt"""
        start_time = time.time()
        
        try:
            # Import image generator
            from utils.image_generator import generate_image
            
            output_dir = os.path.dirname(output_path)
            if output_dir:
                self.safe_create_directory(output_dir)
            
            logger.info(f"🎬 Generating video for: '{prompt}' with style: {style}")
            logger.info(f"💾 Output path: {output_path}")
            
            # Generate base image
            temp_image_path = "temp_video_frame.png"
            image_result = generate_image(
                prompt=prompt,
                style=style,
                enhance_prompt=enhance_prompt,
                output_path=temp_image_path
            )
            
            if not image_result['success']:
                logger.warning("🔄 Creating fallback video due to image generation failure")
                if self.create_fallback_video(prompt, style, output_path, duration):
                    return {
                        'success': True,
                        'video_path': output_path,
                        'enhanced_prompt': prompt,
                        'generation_time': time.time() - start_time,
                        'note': 'Fallback video - AI generation failed'
                    }
                else:
                    return {
                        'success': False,
                        'error': 'Video generation failed at image creation stage'
                    }
            
            # Load the generated image
            base_image = cv2.imread(temp_image_path)
            if base_image is None:
                logger.error("❌ Failed to load generated image")
                return {
                    'success': False,
                    'error': 'Failed to load generated image'
                }
            
            base_image = cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB)
            height, width = base_image.shape[:2]
            
            logger.info(f"📐 Image dimensions: {width}x{height}")
            
            # Create zoom effect frames
            fps = 8
            total_frames = int(duration * fps)
            zoom_factors = np.linspace(1.0, 1.2, total_frames)
            
            frames = []
            for i, zoom in enumerate(zoom_factors):
                new_width = int(width / zoom)
                new_height = int(height / zoom)
                left = (width - new_width) // 2
                top = (height - new_height) // 2
                right = left + new_width
                bottom = top + new_height
                
                # Ensure coordinates are within bounds
                left = max(0, left)
                top = max(0, top)
                right = min(width, right)
                bottom = min(height, bottom)
                
                cropped = base_image[top:bottom, left:right]
                resized = cv2.resize(cropped, (width, height))
                frames.append(resized)
                
                if i % 10 == 0:  # Log progress every 10 frames
                    logger.info(f"🎞️ Generated frame {i+1}/{total_frames}")
            
            # Create video
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
            
            for i, frame in enumerate(frames):
                frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                video_writer.write(frame_bgr)
                
                if i % 10 == 0:  # Log progress every 10 frames
                    logger.info(f"📹 Writing frame {i+1}/{total_frames}")
            
            video_writer.release()
            
            # Clean up temp file
            try:
                if os.path.exists(temp_image_path):
                    os.remove(temp_image_path)
                    logger.info("🧹 Cleaned up temporary image file")
            except Exception as e:
                logger.warning(f"⚠️ Could not remove temp file: {e}")
            
            generation_time = time.time() - start_time
            logger.info(f"✅ Video generated successfully in {generation_time:.2f}s")
            logger.info(f"📁 Video saved to: {output_path}")
            
            return {
                'success': True,
                'video_path': output_path,
                'enhanced_prompt': image_result.get('enhanced_prompt', prompt),
                'generation_time': generation_time
            }
            
        except Exception as e:
            logger.error(f"❌ VIDEO GENERATION FAILED: {str(e)}")
            logger.error(f"🔍 Full error: {traceback.format_exc()}")
            
            # Clean up temp file
            try:
                if os.path.exists("temp_video_frame.png"):
                    os.remove("temp_video_frame.png")
            except:
                pass
            
            # Try fallback video
            if self.create_fallback_video(prompt, style, output_path, duration):
                return {
                    'success': True,
                    'video_path': output_path,
                    'enhanced_prompt': prompt,
                    'generation_time': time.time() - start_time,
                    'note': 'Fallback video - AI generation failed'
                }
            else:
                return {
                    'success': False,
                    'error': f"Video generation failed: {str(e)}"
                }

# Global instance
video_generator = VideoGenerator()

def generate_video(prompt, style="realistic", duration=4, enhance_prompt=False, output_path="output.mp4"):
    return video_generator.generate(prompt, style, duration, enhance_prompt, output_path)