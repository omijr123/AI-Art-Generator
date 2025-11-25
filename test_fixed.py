# test_fixed.py
import torch
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_fixed_model():
    """Test with the tiny model but fixed settings"""
    try:
        from diffusers import DiffusionPipeline
        import torch
        
        logger.info("🔄 Testing with tiny model (fixed settings)...")
        
        # Use the tiny model
        pipe = DiffusionPipeline.from_pretrained(
            "hf-internal-testing/tiny-stable-diffusion-pipe",
            torch_dtype=torch.float32
        )
        
        logger.info("✅ Tiny model loaded!")
        
        # Test generation with correct size for this model
        logger.info("Generating test image...")
        image = pipe(
            "a simple test", 
            num_inference_steps=5,
            width=64,  # Use small size that should work
            height=64
        ).images[0]
        
        # Save the test image
        image.save("test_output.png")
        logger.info("✅ Test image generated and saved as test_output.png!")
        
        return True
    except Exception as e:
        logger.error(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Running fixed test...")
    test_fixed_model()