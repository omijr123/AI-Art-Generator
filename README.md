# 🎨 AI Art Generator - Web & Android

<div align="center">

![AI Art Generator](https://img.shields.io/badge/AI-Art%20Generator-blueviolet)
![Flask](https://img.shields.io/badge/Web-Flask-green)
![Android](https://img.shields.io/badge/Mobile-Android%20Studio-brightgreen)
![Stable Diffusion](https://img.shields.io/badge/AI-Stable%20Diffusion-orange)
![Java](https://img.shields.io/badge/Language-Java-red)
![Python](https://img.shields.io/badge/Language-Python-yellow)

**Transform your imagination into stunning visual art with AI-powered image and video generation**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Gallery](#-gallery) • [Contributing](#-contributing)

</div>

## ✨ Overview

**AI Art Generator** is a powerful cross-platform application that leverages **Stable Diffusion AI** to create breathtaking images and videos from text descriptions. Available as both a **web application** (built with Flask) and a **native Android app** (built with Java), this project brings cutting-edge AI art generation to multiple platforms.

> **"Transforming imagination into reality, one prompt at a time"** ✨

---

## 🚀 Features

### 🖼️ Core Capabilities (Both Platforms)
- **Text-to-Image Generation** - Convert text prompts into high-quality images
- **Text-to-Video Generation** - Create dynamic videos with smooth zoom effects
- **Multiple Art Styles** - Realistic, Anime, Cinematic, 3D Render, Oil Painting, Sketch
- **AI Prompt Enhancement** - Automatically improve prompts for better results
- **Real-time Generation** - Watch as your creations come to life
- **Save & Share** - Download results to gallery or share directly

### 🌐 Web Version (Flask)
- **Responsive Design** - Beautiful UI that works on all devices
- **Dark/Light Mode** - Customizable theme preferences
- **Instant Downloads** - One-click download for generated content
- **RESTful API** - Clean backend architecture
- **Progress Tracking** - Real-time generation progress

### 📱 Android App (Java)
- **Native Performance** - Optimized for mobile devices
- **Material Design** - Modern Android UI/UX following Google's design principles
- **Gallery Integration** - Save directly to device gallery
- **Offline Capabilities** - Generate art without internet connection
- **Push Notifications** - Get notified when generation completes
- **Hugging Face API** - State-of-the-art AI model integration

---

## 🛠️ Technology Stack

### Web Version
| Component | Technology |
|-----------|------------|
| **Backend** | Python, Flask |
| **AI Model** | Stable Diffusion v1.5 |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Video Processing** | OpenCV, FFmpeg |
| **Styling** | CSS Variables, Flexbox, Grid |

### Android App
| Component | Technology |
|-----------|------------|
| **Language** | Java |
| **Framework** | Android SDK |
| **Architecture** | MVVM Pattern |
| **API Integration** | Retrofit, OkHttp |
| **Image Processing** | Glide, Bitmap Factory |
| **AI Service** | Hugging Face API |

---

## 📥 Installation & Setup

### 🌐 Web Version Setup

```bash
# Clone the repository
git clone https://github.com/omijr123/AI-Art-Generator.git
cd AI-Art-Generator/web-version

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

**Web Requirements:**
- Python 3.8+
- Flask 2.3+
- OpenCV 4.5+
- PyTorch 1.12+
- Stable Diffusion model files

### 📱 Android App Setup

```bash
# Clone the repository
git clone https://github.com/omijr123/AI-Art-Generator.git
cd AI-Art-Generator/android-app

# Open in Android Studio
# Build and run on device/emulator
```

**Android Requirements:**
- Android Studio Arctic Fox+
- Android SDK 30+
- Java 11+
- Minimum API Level: 21

### 🔐 API Key Setup (Android)

To use the Hugging Face AI services in the Android app:

1. Create a Hugging Face account at [huggingface.co](https://huggingface.co)
2. Go to: [Settings → Access Tokens](https://huggingface.co/settings/tokens)
3. Generate a new token
4. Add it to your API client:

```java
headers.put("Authorization", "Bearer YOUR_API_KEY");
```

---

## 🎯 Usage

### Web Version
1. **Enter Prompt** - Describe what you want to create
2. **Choose Style** - Select from multiple art styles
3. **Set Duration** - Choose video length (3-6 seconds)
4. **Generate** - Click "Generate Image" or "Generate Video"
5. **Download** - Save your creation with one click

### Android App
1. **Launch App** - Open the AI Art Generator app
2. **Describe Vision** - Type your creative prompt
3. **Customize Settings** - Adjust style and preferences
4. **Generate Art** - Create and view your artwork
5. **Save & Share** - Store in gallery or share with friends

---

## 📸 Gallery

### 🎨 Generated Artwork Examples

<div align="center">

#### Realistic Style
![Realistic Image 1](https://i.postimg.cc/BnDfmGqC/1.jpg)
![Realistic Image 2](https://i.postimg.cc/0QCwm36B/2.jpg)

#### Anime Style
![Anime Image 1](https://i.postimg.cc/ydWHX3W8/1.png)
![Anime Image 2](https://i.postimg.cc/HLkxRxj4/2.png)

#### Cinematic Style
![Cinematic Image 1](https://i.postimg.cc/mrfjyvDB/1.png)
![Cinematic Image 2](https://i.postimg.cc/fTVvnzSs/2.png)

#### 3D Render Style
![3D Render 1](https://i.postimg.cc/8sgc0mrt/1.png)
![3D Render 2](https://i.postimg.cc/63T0hnRJ/2.png)

#### Oil Painting Style
![Oil Painting 1](https://i.postimg.cc/rw3FmLjL/1.png)
![Oil Painting 2](https://i.postimg.cc/0Q531zwV/2.png)

#### Sketch Style
![Sketch 1](https://i.postimg.cc/pXkJ3sZT/1.png)

</div>

### 📱 App Interfaces

<div align="center">

#### Android App
![Android UI 1](https://i.postimg.cc/3N9kqvYG/1.jpg)
![Android UI 2](https://i.postimg.cc/05ZrP71G/2.jpg)

#### Web App
![Web UI 1](https://i.postimg.cc/d0HkndQR/1.png)
![Web UI 2](https://i.postimg.cc/ncJz4TKT/2.png)

#### Development Environment
![Android Studio](https://i.postimg.cc/PxXhRFx6/1.png)
![VS Code](https://i.postimg.cc/zfs5JX0j/1.png)

</div>

---

## 🎨 Example Prompts

### Great Prompts for Best Results:
```
🏔️ "A majestic dragon soaring over medieval castle, fantasy art, highly detailed, dramatic lighting"

🌃 "Cyberpunk cityscape at night, neon lights, rain-soaked streets, futuristic architecture"

🧙 "Portrait of an elderly wizard with long white beard, magical glow, cinematic lighting"

🌸 "Serene Japanese garden with cherry blossoms, traditional architecture, peaceful atmosphere"

🎨 "Van Gogh style starry night over a modern city, impressionist brush strokes"

🚀 "Astronaut riding a horse on Mars, surrealism, photorealistic, 4k"
```

### Tips for Better Results:
- Be descriptive and specific
- Include style references (e.g., "oil painting", "anime style")
- Mention lighting and mood
- Specify composition and perspective
- Use the "Enhance prompt" feature

---

## 📁 Project Structure

```
AI-Art-Generator/
│
├── web-version/                 # Flask Web Application
│   ├── app.py                  # Main Flask application
│   ├── utils/
│   │   ├── image_generator.py  # AI image generation
│   │   └── video_generator.py  # Video creation & processing
│   ├── templates/
│   │   └── index.html          # Main web interface
│   ├── static/
│   │   ├── style.css           # Responsive styling
│   │   └── script.js           # Frontend functionality
│   └── generated/              # Output directory
│       ├── images/             # Generated images
│       └── videos/             # Generated videos
│
├── android-app/                # Native Android Application
│   ├── app/src/main/java/
│   │   ├── activities/         # Android activities
│   │   ├── adapters/           # RecyclerView adapters
│   │   ├── api/                # API clients (Retrofit)
│   │   ├── models/             # Data models
│   │   └── utils/              # Utility classes
│   ├── app/src/main/res/
│   │   ├── layout/             # XML layouts
│   │   ├── drawable/           # Images and icons
│   │   └── values/             # Strings, colors, styles
│   └── build.gradle            # Dependencies configuration
│
└── docs/                       # Documentation
    ├── screenshots/            # App previews
    └── technical/              # Technical details
```

---

## ⚡ How It Works

### Web Version Flow:
1. User enters prompt → Flask backend processes request
2. Stable Diffusion generates image → OpenCV creates video frames
3. Video compilation → Results served via web interface
4. User downloads or views directly in browser

### Android App Flow:
1. User input → Java processing and validation
2. API call to Hugging Face → AI model generates image
3. Image processing and optimization → Display in RecyclerView
4. Save to gallery or share via Android intents

---

## 🤝 Contributing

We love contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### 🛠️ Development Areas Needed:
- 🖌️ New art styles and filters
- 📱 Enhanced mobile features (camera integration, AR)
- 🎥 Advanced video effects and transitions
- 🔧 Performance optimization for faster generation
- 🌍 Multi-language support
- ☁️ Cloud storage integration
- 🔒 Enhanced security and privacy features

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- **Stable Diffusion** team for the revolutionary AI model
- **Hugging Face** for providing accessible AI APIs
- **Flask** community for the excellent web framework
- **Android Developer** community for continuous support
- **OpenCV** for robust video processing capabilities
- All contributors and testers who helped improve this project

---

<div align="center">

## 📞 Support

If you have any questions or need help with setup, please open an issue on GitHub.

### ⭐ Don't forget to star this repository if you find it helpful!

**"Creativity meets technology - bringing your imagination to life"** 🚀

</div>

---

*Last updated: November 2024*  
*Built with ❤️ using Java, Android Studio, Python, and Flask*
