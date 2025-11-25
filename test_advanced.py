# test_advanced.py
import logging
from utils.image_generator import generate_image
from utils.video_generator import generate_video

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_advanced_generator():
    """Test the advanced generator"""
    print("🧪 Testing advanced image generator...")
    
    # Test image generation
    result = generate_image(
        prompt="a beautiful sunset over mountains",
        style="cinematic",
        output_path="test_advanced_image.png"
    )
    
    if result['success']:
        print("✅ Advanced image generator works!")
        print(f"   Image saved as: {result['image_path']}")
        print(f"   Note: {result.get('note', 'No note')}")
    else:
        print(f"❌ Advanced image failed: {result['error']}")
    
    # Test video generation
    print("\n🧪 Testing advanced video generator...")
    
    result = generate_video(
        prompt="a spaceship flying through space",
        style="3d_render", 
        duration=2,
        output_path="test_advanced_video.mp4"
    )
    
    if result['success']:
        print("✅ Advanced video generator works!")
        print(f"   Video saved as: {result['video_path']}")
        print(f"   Note: {result.get('note', 'No note')}")
    else:
        print(f"❌ Advanced video failed: {result['error']}")

if __name__ == "__main__":
    test_advanced_generator()