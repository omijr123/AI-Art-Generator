from flask import Flask, render_template, request, jsonify, send_file
import os
import uuid
from datetime import datetime
import logging
import errno

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def create_directories_safe():
    directories = ['generated/images', 'generated/videos', 'static', 'templates']
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"✅ Created/verified directory: {directory}")
        except OSError as e:
            logger.error(f"❌ Error creating directory {directory}: {e}")

create_directories_safe()

try:
    from utils.image_generator import generate_image
    logger.info("✅ AI Image generator imported successfully")
except ImportError as e:
    logger.error(f"❌ Failed to import image generator: {e}")
    def generate_image(*args, **kwargs):
        return {'success': False, 'error': 'Image generator not available'}

try:
    from utils.video_generator import generate_video
    logger.info("✅ Video generator imported successfully")
except ImportError as e:
    logger.error(f"❌ Failed to import video generator: {e}")
    def generate_video(*args, **kwargs):
        return {'success': False, 'error': 'Video generator not available'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/image', methods=['POST'])
def generate_image_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        prompt = data.get('prompt', '')
        style = data.get('style', 'realistic')
        enhance_prompt = data.get('enhance_prompt', False)
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        logger.info(f"🔄 Received image generation request: '{prompt}' with style: {style}")
        
        filename = f"image_{uuid.uuid4().hex[:8]}.png"
        filepath = os.path.join('generated/images', filename)
        
        result = generate_image(
            prompt=prompt,
            style=style,
            enhance_prompt=enhance_prompt,
            output_path=filepath
        )
        
        if result.get('success'):
            response_data = {
                'success': True,
                'image_url': f'/generated/images/{filename}',
                'prompt_used': result.get('enhanced_prompt', prompt),
                'generation_time': round(result.get('generation_time', 0), 2),
                'model': 'runwayml/stable-diffusion-v1-5'
            }
            if result.get('note'):
                response_data['note'] = result['note']
            
            logger.info(f"✅ Image generation completed in {response_data['generation_time']}s")
            return jsonify(response_data)
        else:
            logger.error(f"❌ Image generation failed: {result.get('error')}")
            return jsonify({'error': result.get('error', 'Image generation failed')}), 500
            
    except Exception as e:
        logger.error(f"❌ Unexpected error in image generation: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/generate/video', methods=['POST'])
def generate_video_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        prompt = data.get('prompt', '')
        style = data.get('style', 'realistic')
        duration = data.get('duration', 4)
        enhance_prompt = data.get('enhance_prompt', False)
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        logger.info(f"🔄 Received video generation request: '{prompt}' with style: {style}")
        
        filename = f"video_{uuid.uuid4().hex[:8]}.mp4"
        filepath = os.path.join('generated/videos', filename)
        
        result = generate_video(
            prompt=prompt,
            style=style,
            duration=duration,
            enhance_prompt=enhance_prompt,
            output_path=filepath
        )
        
        if result.get('success'):
            response_data = {
                'success': True,
                'video_url': f'/generated/videos/{filename}',
                'prompt_used': result.get('enhanced_prompt', prompt),
                'generation_time': round(result.get('generation_time', 0), 2),
                'model': 'runwayml/stable-diffusion-v1-5'
            }
            if result.get('note'):
                response_data['note'] = result['note']
            
            logger.info(f"✅ Video generation completed in {response_data['generation_time']}s")
            return jsonify(response_data)
        else:
            logger.error(f"❌ Video generation failed: {result.get('error')}")
            return jsonify({'error': result.get('error', 'Video generation failed')}), 500
            
    except Exception as e:
        logger.error(f"❌ Unexpected error in video generation: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/generated/images/<filename>')
def serve_image(filename):
    try:
        image_path = os.path.join('generated/images', filename)
        logger.info(f"📤 Serving image: {image_path}")
        return send_file(image_path, mimetype='image/png')
    except FileNotFoundError:
        logger.error(f"❌ Image not found: {filename}")
        return jsonify({'error': 'Image not found'}), 404
    except Exception as e:
        logger.error(f"❌ Error serving image: {str(e)}")
        return jsonify({'error': 'Error serving image'}), 500

@app.route('/generated/videos/<filename>')
def serve_video(filename):
    try:
        video_path = os.path.join('generated/videos', filename)
        logger.info(f"📤 Serving video: {video_path}")
        
        # Check if file exists
        if not os.path.exists(video_path):
            logger.error(f"❌ Video file not found: {video_path}")
            return jsonify({'error': 'Video not found'}), 404
            
        return send_file(video_path, mimetype='video/mp4')
        
    except FileNotFoundError:
        logger.error(f"❌ Video not found: {filename}")
        return jsonify({'error': 'Video not found'}), 404
    except Exception as e:
        logger.error(f"❌ Error serving video: {str(e)}")
        return jsonify({'error': 'Error serving video'}), 500

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy', 
        'timestamp': datetime.now().isoformat(),
        'model': 'runwayml/stable-diffusion-v1-5',
        'directories': {
            'images': os.path.exists('generated/images'),
            'videos': os.path.exists('generated/videos')
        }
    })

if __name__ == '__main__':
    logger.info("🚀 Starting AI Art Generator...")
    logger.info("🧠 Using model: runwayml/stable-diffusion-v1-5")
    logger.info("💡 First generation may take 2-5 minutes to download model")
    logger.info("📱 Subsequent generations will be faster (30-60 seconds)")
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)