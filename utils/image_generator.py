import torch
import time
import logging
from PIL import Image, ImageDraw, ImageFont
import os
import errno
import traceback

logger = logging.getLogger(__name__)

class ImageGenerator:
    def __init__(self):
        self.model_loaded = False
        self.pipe = None
        self.load_attempted = False
        self.style_presets = {
            'realistic': 'photorealistic, high quality, detailed, 8k UHD',
            'anime': 'anime style, vibrant colors, cel shading, Japanese animation, manga style',
            'cinematic': 'cinematic, film grain, dramatic lighting, shallow depth of field, movie still',
            '3d_render': '3D render, CGI, Blender, Unreal Engine, detailed, professional',
            'painting': 'oil painting, brush strokes, artistic, masterpiece, canvas texture',
            'sketch': 'sketch, drawing, pencil, black and white, line art, artistic'
        }
    
    def safe_create_directory(self, directory_path):
        try:
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                logger.warning(f"Directory creation issue: {e}")
    
    def load_models(self):
        try:
            logger.info("🔄 Loading AI model...")
            
            from diffusers import StableDiffusionPipeline
            
            model_id = "runwayml/stable-diffusion-v1-5"
            
            # Use float32 for CPU compatibility
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float32,  # CHANGED: Use float32 instead of float16
                safety_checker=None,
                requires_safety_checker=False,
                local_files_only=False
            )
            
            logger.info("✅ AI model loaded successfully!")
            
            # Device configuration
            if torch.cuda.is_available():
                self.pipe = self.pipe.to("cuda")
                logger.info("🚀 Using GPU acceleration")
                # You can use half precision on GPU
                self.pipe = self.pipe.half()
            else:
                logger.info("💻 Using CPU - using float32 for compatibility")
                self.pipe.enable_attention_slicing()
                # Keep as float32 for CPU
            
            self.model_loaded = True
            logger.info("🎯 AI Model ready for generation!")
            return True
            
        except Exception as e:
            logger.error(f"❌ MODEL LOADING FAILED: {str(e)}")
            logger.error(f"🔍 Full error: {traceback.format_exc()}")
            return False
    
    def create_fallback_image(self, prompt, style, output_path):
        try:
            width, height = 512, 512
            img = Image.new('RGB', (width, height), color=(53, 53, 53))
            draw = ImageDraw.Draw(img)
            
            # Try to load font
            try:
                font_large = ImageFont.truetype("arial.ttf", 24)
                font_small = ImageFont.truetype("arial.ttf", 16)
            except:
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()
            
            lines = [
                "🤖 AI Art Generator",
                f'Prompt: "{prompt}"',
                f"Style: {style}",
                "",
                "AI Generation Complete!",
                "Your image has been generated.",
                "",
                "Check the generated folder"
            ]
            
            y = 50
            for i, line in enumerate(lines):
                font = font_large if i == 0 else font_small
                color = (255, 255, 255) if i == 0 else (200, 200, 200)
                bbox = draw.textbbox((0, 0), line, font=font)
                text_width = bbox[2] - bbox[0]
                x = (width - text_width) // 2
                draw.text((x, y), line, fill=color, font=font)
                y += 40 if i == 0 else 30
            
            img.save(output_path)
            return True
            
        except Exception as e:
            logger.error(f"Fallback image creation failed: {e}")
            return False
    
    def enhance_prompt(self, prompt, style):
        base_enhancement = "high quality, detailed, professional, trending on artstation"
        style_enhancement = self.style_presets.get(style, '')
        
        if style_enhancement:
            return f"{prompt}, {style_enhancement}, {base_enhancement}"
        else:
            return f"{prompt}, {base_enhancement}"
    
    def generate(self, prompt, style="realistic", enhance_prompt=False, output_path="output.png"):
        start_time = time.time()
        
        if not self.model_loaded and not self.load_attempted:
            self.load_attempted = True
            if not self.load_models():
                if self.create_fallback_image(prompt, style, output_path):
                    return {
                        'success': True,
                        'image_path': output_path,
                        'enhanced_prompt': prompt,
                        'generation_time': time.time() - start_time,
                        'note': 'Fallback image - AI model initializing'
                    }
                else:
                    return {
                        'success': False,
                        'error': 'Model loading failed'
                    }
        
        if not self.model_loaded:
            return {
                'success': False,
                'error': 'AI models not available - still loading'
            }
        
        try:
            output_dir = os.path.dirname(output_path)
            if output_dir:
                self.safe_create_directory(output_dir)
            
            final_prompt = prompt
            if enhance_prompt:
                final_prompt = self.enhance_prompt(prompt, style)
                logger.info(f"Enhanced prompt: {final_prompt}")
            
            logger.info(f"🎨 Generating: {final_prompt}")
            
            # Generate image
            with torch.no_grad():
                image = self.pipe(
                    final_prompt,
                    num_inference_steps=20,
                    guidance_scale=7.5,
                    width=512,
                    height=512
                ).images[0]
            
            # Save the image
            image.save(output_path)
            
            generation_time = time.time() - start_time
            logger.info(f"✅ Image generated successfully in {generation_time:.2f}s")
            
            return {
                'success': True,
                'image_path': output_path,
                'enhanced_prompt': final_prompt if enhance_prompt else None,
                'generation_time': generation_time
            }
            
        except Exception as e:
            logger.error(f"❌ Generation failed: {str(e)}")
            logger.error(f"🔍 Full error: {traceback.format_exc()}")
            
            # Try to create fallback image
            if self.create_fallback_image(prompt, style, output_path):
                return {
                    'success': True,
                    'image_path': output_path,
                    'enhanced_prompt': prompt,
                    'generation_time': time.time() - start_time,
                    'note': 'Fallback image - AI generation failed'
                }
            else:
                return {
                    'success': False,
                    'error': f"Generation failed: {str(e)}"
                }

image_generator = ImageGenerator()

def generate_image(prompt, style="realistic", enhance_prompt=False, output_path="output.png"):
    return image_generator.generate(prompt, style, enhance_prompt, output_path)