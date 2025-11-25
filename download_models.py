# download_models.py
#!/usr/bin/env python3
"""
Pre-download models to avoid timeout during first generation
"""
import os
import logging
import sys
import requests
import time
import threading
import signal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TimeoutError(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutError("Model loading timed out")

def download_models_with_timeout(timeout_seconds=300):
    """Pre-download the models with timeout"""
    # Set up timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)
    
    try:
        logger.info("📥 Checking if models can be downloaded...")
        
        # Test Hugging Face access
        test_url = "https://huggingface.co/api/models/runwayml/stable-diffusion-v1-5"
        try:
            response = requests.get(test_url, timeout=10)
            if response.status_code == 200:
                logger.info("✅ Can access Hugging Face Hub")
            else:
                logger.warning(f"⚠️ Hugging Face access issue: {response.status_code}")
        except Exception as e:
            logger.warning(f"⚠️ Cannot access Hugging Face: {e}")
        
        logger.info("🔄 Testing with a small model first...")
        
        from diffusers import StableDiffusionPipeline
        import torch
        
        model_id = "runwayml/stable-diffusion-v1-5"
        
        logger.info(f"🔄 Downloading model: {model_id}")
        logger.info("⏰ This may take 2-5 minutes...")
        
        # Remove problematic parameters
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32,
            safety_checker=None,
            use_safetensors=True,
            local_files_only=False
        )
        
        logger.info("✅ Model downloaded successfully!")
        
        # Quick test
        logger.info("🧪 Quick model test...")
        with torch.no_grad():
            test_image = pipe(
                "test",
                num_inference_steps=2,
                guidance_scale=1.0,
                width=64,
                height=64
            ).images[0]
        
        logger.info("✅ Model test passed!")
        
        # Clean up
        del pipe
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            
        signal.alarm(0)  # Cancel timeout
        return True
        
    except TimeoutError:
        logger.error(f"❌ Model loading timed out after {timeout_seconds} seconds")
        return False
    except Exception as e:
        logger.error(f"❌ Model download failed: {e}")
        signal.alarm(0)  # Cancel timeout
        return False

def download_models():
    """Main download function with fallbacks"""
    try:
        # Try with timeout
        success = download_models_with_timeout(300)  # 5 minute timeout
        
        if not success:
            logger.info("💡 Trying alternative approach...")
            # Try a different method
            return download_models_alternative()
        
        return True
        
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return False

def download_models_alternative():
    """Alternative download method"""
    try:
        logger.info("🔄 Trying alternative model download...")
        
        # Try a smaller model first
        from diffusers import DiffusionPipeline
        import torch
        
        model_id = "OFA-Sys/small-stable-diffusion-v0"  # Smaller model
        
        logger.info(f"🔄 Downloading smaller model: {model_id}")
        
        pipe = DiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32,
            use_safetensors=True
        )
        
        logger.info("✅ Alternative model downloaded successfully!")
        return True
        
    except Exception as e:
        logger.error(f"❌ Alternative model also failed: {e}")
        return False

if __name__ == "__main__":
    logger.info("🚀 Starting model download check...")
    success = download_models()
    
    if success:
        logger.info("🎉 Model preparation completed!")
        sys.exit(0)
    else:
        logger.info("ℹ️ Models will be downloaded when first used")
        logger.info("💡 You can still run the application")
        sys.exit(1)