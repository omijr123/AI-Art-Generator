import subprocess
import sys
import os

def install_requirements():
    """Install required packages with error handling"""
    
    requirements = [
        "flask==2.3.3",
        "torch==2.1.2",
        "torchvision==0.16.2", 
        "torchaudio==2.1.2",
        "transformers==4.35.2",
        "diffusers==0.25.0",
        "accelerate==0.25.0",
        "pillow==10.1.0",
        "opencv-python==4.8.1.78",
        "numpy==1.24.3",
        "requests==2.31.0",
        "python-dotenv==1.0.0"
    ]
    
    print("Installing required packages...")
    
    for package in requirements:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")
            # Try without version specifier
            package_name = package.split('==')[0]
            try:
                print(f"Trying to install {package_name} without version constraint...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            except subprocess.CalledProcessError:
                print(f"Could not install {package_name}")
    
    print("Installation completed!")

if __name__ == "__main__":
    install_requirements()