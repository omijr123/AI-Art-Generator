# test_simple.py
import torch
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_basic_imports():
    """Test if basic imports work"""
    try:
        import diffusers
        import transformers
        import torch
        logger.info("✅ Basic imports work")
        return True
    except Exception as e:
        logger.error(f"❌ Basic imports failed: {e}")
        return False

def test_small_model():
    """Test with a very small model"""
    try:
        from diffusers import DiffusionPipeline
        import torch
        
        logger.info("🔄 Testing with tiny model...")
        
        # Use a very small model
        pipe = DiffusionPipeline.from_pretrained(
            "hf-internal-testing/tiny-stable-diffusion-pipe",
            torch_dtype=torch.float32
        )
        
        logger.info("✅ Tiny model loaded!")
        
        # Test generation
        image = pipe("test").images[0]
        logger.info("✅ Tiny model generation works!")
        
        return True
    except Exception as e:
        logger.error(f"❌ Tiny model failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Running basic tests...")
    
    if test_basic_imports():
        test_small_model()