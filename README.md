
# 🎨 AI Art Generator – Web & Android (Java + Python)

<div align="center">

![AI Art Generator](https://img.shields.io/badge/AI-Art%20Generator-blueviolet)
![Android](https://img.shields.io/badge/Mobile-Android%20Studio-brightgreen)
![Flask](https://img.shields.io/badge/Web-Flask-green)
![Java](https://img.shields.io/badge/Language-Java-red)
![Python](https://img.shields.io/badge/Language-Python-yellow)
![Stable Diffusion](https://img.shields.io/badge/Model-Stable%20Diffusion-orange)

**Transform your imagination into stunning AI-generated images & videos**

</div>

---

## ✨ Overview

**AI Art Generator** is a cross-platform AI-powered application built for:

* 🌐 **Web** (Flask + Python)
* 📱 **Android App** (Java + Android Studio)

Users can enter a text prompt, select a style, and generate:

* **AI Images** (High Quality)
* **AI Zoom Videos** (Animated)

The backend uses **Stable Diffusion** & **Hugging Face Inference API** to generate outputs in multiple art styles.

---

# 📱 Android App Preview

<div align="center">

### -- App UI Interface --

![pic1](https://i.postimg.cc/3N9kqvYG/1.jpg)
![pic2](https://i.postimg.cc/05ZrP71G/2.jpg)



### -- Android Studio Working Space --



![pic3](https://i.postimg.cc/PxXhRFx6/1.png)



![pic4](https://i.postimg.cc/1zyLmVZT/2.png)



![pic5](https://i.postimg.cc/bvC849td/5.png)



### -- Android Studio (Results Screen) --

![pic6](https://i.postimg.cc/g05QvShZ/7.png)

</div>

---


# 🌐 Web App Preview

<div align="center">

### -- Web App UI Interface --

![pic1](https://i.postimg.cc/d0HkndQR/1.png)

![pic2](https://i.postimg.cc/ncJz4TKT/2.png)


### -- VS Code Working Space --

![pic3](https://i.postimg.cc/zfs5JX0j/1.png)

![pic4](https://i.postimg.cc/B65W458j/2.png)

![pic5](https://i.postimg.cc/13Vjy025/7.png)

### -- VS Code (Generated Results) --

![pic6](https://i.postimg.cc/6pxdGdTT/9.png)


![pic7](https://i.postimg.cc/3W5DmT8G/10.png)

</div>

---

# 📱 Output Results Preview (Option B Format)

---

## 📂 **Category 1: Realistic**

### 🖼️ Images Output

* ![img](https://i.postimg.cc/BnDfmGqC/1.jpg)
  
* ![img](https://i.postimg.cc/0QCwm36B/2.jpg)

### 🎥 Videos Output

* ![vid](https://i.postimg.cc/q7VhF02J/1.jpg)
  
* ![vid](https://i.postimg.cc/B6NjtKkQ/2.png)

---

## 📂 **Category 2: Anime**

### 🖼️ Images Output

* ![img](https://i.postimg.cc/ydWHX3W8/1.png)
  
* ![img](https://i.postimg.cc/HLkxRxj4/2.png)

### 🎥 Videos Output

* ![vid](https://i.postimg.cc/2S8r8tmL/1.png)
  
* ![vid](https://i.postimg.cc/9FcjJk4j/2.png)

---

## 📂 **Category 3: Cinematic**

### 🖼️ Images Output

* ![img](https://i.postimg.cc/mrfjyvDB/1.png)
  
* ![img](https://i.postimg.cc/fTVvnzSs/2.png)

### 🎥 Videos Output

* ![vid](https://i.postimg.cc/gcTvKCtp/1.png)
  
* ![vid](https://i.postimg.cc/FRKLypjk/2.png)

---

## 📂 **Category 4: 3D Render**

### 🖼️ Images Output

* ![img](https://i.postimg.cc/8sgc0mrt/1.png)
  
* ![img](https://i.postimg.cc/63T0hnRJ/2.png)

### 🎥 Videos Output

* ![vid](https://i.postimg.cc/FRfySm59/1.png)
  
* ![vid](https://i.postimg.cc/t4XF5FGy/2.png)

---

## 📂 **Category 5: Oil Painting**

### 🖼️ Images Output

* ![img](https://i.postimg.cc/rw3FmLjL/1.png)
  
* ![img](https://i.postimg.cc/0Q531zwV/2.png)

### 🎥 Videos Output

* ![vid](https://i.postimg.cc/wvbWK0HM/1.png)
  
* ![vid](https://i.postimg.cc/jSbYkdMq/2.png)

---

## 📂 **Category 6: Sketch**

### 🖼️ Images Output

* ![img](https://i.postimg.cc/pXkJ3sZT/1.png)

### 🎥 Videos Output

![vid](https://i.postimg.cc/R0tfCdcF/1.png)
  
![vid](https://i.postimg.cc/Sx2YVd1P/2.png)

---

# 🚀 Features

### ⭐ Core Features (Both Web & Android)

* Text-to-Image generation
* Text-to-Video (AI Zoom Animation)
* Multiple Art Styles
* Fast cloud inference with Hugging Face
* Save, Share & Re-generate options
* Clean UI + smooth experience

### 🌐 Web App Features

* Flask backend for AI processing
* Async generation (non-blocking)
* Auto-download of results
* Real-time progress indicators

### 📱 Android App Features

* Built using **Java + Android SDK**
* Material UI
* Retrofit API integration
* Glide for fast image loading
* Local storage for downloads

---

# 🛠️ Tech Stack

### 🧠 Backend (AI)

* Stable Diffusion
* Hugging Face Inference API
* Diffusers
* OpenCV (video animation)

### 🌐 Web

* Python
* Flask
* HTML/CSS/JavaScript

### 📱 Android

* Java
* Android Studio
* Retrofit
* Glide
* MVVM architecture

---

# 📥 Installation & Setup

## 🖥️ Web (Flask)

```bash
git clone <repo-url>
cd web
pip install -r requirements.txt
python app.py
```

Access at:

```
http://127.0.0.1:5000/
```

---

## 📱 Android App

1. Open **Android Studio**
2. Select **Open Project**
3. Choose the `AndroidApp/` folder
4. Build Gradle
5. Add your Hugging Face API key in:

```
ApiClient.java
```

6. Run on Emulator or Physical Device

---

# 🎯 Usage

1. Enter your **text prompt**
2. Select **Art Style**
3. Choose:

   * **Generate Image**
   * **Generate Video**
4. Wait for AI to process
5. Download or share the result

---

# 📁 Project Structure

```
AIArtGenerator/
│
├── Web/
│   ├── app.py
│   ├── static/
│   ├── templates/
│   ├── models/
│   └── utils/
│
├── Android/
│   ├── app/
│   ├── java/
│   ├── res/
│   └── manifest.xml
│
└── README.md
```

---

# 🎨 Example Prompts

* “realistic portrait of a warrior princess, 8k”
* “anime boy walking in neon tokyo”
* “cinematic shot, desert storm, dramatic lighting”
* “3d render of a glowing robot”
* “oil painting of an old king”
* "pencil sketch of a cat wearing glasses"

---

# ⚡ How It Works

1. User sends prompt → App
2. App sends request → Flask / HuggingFace
3. Stable Diffusion generates image/video
4. Flask returns result
5. Android/Web displays output

---

# 🤝 Contributing

Pull requests are welcome!
Feel free to improve UI, add new styles, or optimize backend.

---

# 📄 License

MIT License

---

<div align="center">

## ⭐ If you like this project, give it a star!

**"Creativity meets technology — bringing your imagination to life"**

</div>

---

