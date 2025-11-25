print("Testing AI Art Generation capability...")

try:
    import torch
    print(f"✅ PyTorch {torch.__version__}")
    
    import diffusers
    print(f"✅ Diffusers {diffusers.__version__}")
    
    # Test loading a pipeline
    from diffusers import StableDiffusionPipeline
    
    # Use a small model for testing
    model_id = "runwayml/stable-diffusion-v1-5"
    print(f"🔄 Loading model: {model_id}")
    
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32,
        use_safetensors=True
    )
    print("✅ Model loaded successfully!")
    
    # Test a simple generation
    print("🚀 Testing image generation...")
    prompt = "a beautiful sunset over mountains"
    image = pipe(prompt, num_inference_steps=5).images[0]  # Few steps for quick test
    print("✅ Image generation successful!")
    
    # Save test image
    image.save("test_output.png")
    print("💾 Test image saved as 'test_output.png'")
    
except Exception as e:
    print(f"❌ Error during AI test: {e}")
    print("This is normal if models need to download first.")