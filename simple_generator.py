# simple_generator.py
"""
Simple image generator that always works
"""
import os
import logging
from PIL import Image, ImageDraw, ImageFont
import random

logger = logging.getLogger(__name__)

def create_simple_ai_image(prompt, style, output_path):
    """Create a simple AI-style image that always works"""
    try:
        width, height = 512, 512
        
        # Create base image with random color
        base_color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        image = Image.new('RGB', (width, height), color=base_color)
        draw = ImageDraw.Draw(image)
        
        # Add some "AI-style" elements
        # Gradient effect
        for y in range(height):
            factor = y / height
            r = int(base_color[0] * (1 - factor) + 255 * factor)
            g = int(base_color[1] * (1 - factor) + 255 * factor) 
            b = int(base_color[2] * (1 - factor) + 255 * factor)
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        # Add some random shapes for "artistic" effect
        for _ in range(10):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(x1, width)
            y2 = random.randint(y1, height)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.ellipse([x1, y1, x2, y2], outline=color, width=2)
        
        # Add text
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            try:
                font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
            except:
                font = ImageFont.load_default()
        
        text = f"AI Art\n{prompt}\nStyle: {style}"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        # Text background
        draw.rectangle([x-15, y-15, x+text_width+15, y+text_height+15], fill=(0, 0, 0, 180))
        draw.text((x, y), text, fill=(255, 255, 255), font=font, align="center")
        
        # Save image
        image.save(output_path)
        
        return {
            'success': True,
            'image_path': output_path,
            'enhanced_prompt': prompt,
            'generation_time': 0.2,
            'note': 'Simple AI-style image'
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f"Simple generator failed: {str(e)}"
        }

# Test it
if __name__ == "__main__":
    result = create_simple_ai_image("a beautiful sunset", "realistic", "simple_test.png")
    if result['success']:
        print("✅ Simple generator works! Check simple_test.png")
    else:
        print(f"❌ Simple generator failed: {result['error']}")