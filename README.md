# **Real-Time Indian Sign Language (ISL) to Text & Speech Translator**  
✋🎤 *Real-Time Sign Recognition • Hindi/Bengali/English Voice Output • MediaPipe + Machine Learning*

---

## 📘 **Indian Sign Language (ISL) → Text & Speech Translator**

---

## 🚀 **Project Overview**
This project is a **Real-Time Indian Sign Language (ISL) Recognition System** that converts hand gestures captured through a webcam into **text**, and then into **speech** using **Google Text-to-Speech (gTTS)**.

It uses:

- 🖐 **MediaPipe Hands** for accurate 21–point hand-landmark detection  
- 🤖 **A custom-trained ML model** using hand-landmark features  
- ⚡ **Real-time prediction** with stable frame-consistency  
- 🔊 **Text-to-speech** output in **Hindi**, **Bengali**, and **English**

This project is built to help the **hearing impaired**, **speech impaired**, **children**, and **elderly people** communicate more smoothly.

---

## ✨ **Key Features**

- 🎥 **Real-time ISL Gesture Recognition**  
- 🤖 **Machine Learning Classifier (RandomForest / SVM)**  
- 🔊 **Instant Text-to-Speech Output** in multiple Indian languages  
- 📈 **Confidence Thresholding** for improved accuracy  
- ✋ **Supported Gestures (Initial Version):**  
  - Hello  
  - Yes  
  - No  
  - Thanks  
   
- 🧠 Easy to extend — add more gesture classes anytime  
- 💡 Clean UI overlay showing gesture name  
- 🔧 Smooth & stable predictions using **frame-consistency logic**

---

## 🛠️ **Tech Stack**

- **Python**  
- **OpenCV**  
- **MediaPipe Hands**  
- **NumPy**  
- **Pickle** (Model Serialization)  
- **gTTS (Google Text-to-Speech)**  
- **Pygame** (Audio Playback)

---

## 📦 **Installation**

### **Clone the repository:**
```bash
git clone https://github.com/your-username/isl-sign-language-translator.git
cd isl-sign-language-translator
```

### **Install dependencies:**
```bash
pip install -r requirements.txt
```

### **Add your trained model:**
Place your ML model file inside the project folder:

```
model.p
```

### **Run the application:**
```bash
python main.py
```

---

## 📚 **How It Works**

### 1️⃣ **Hand Landmark Detection**  
MediaPipe extracts **21 key points** from your hand in real-time.

### 2️⃣ **Feature Extraction**  
All coordinates are **normalized** relative to the wrist → stable predictions even if your hand moves.

### 3️⃣ **ML Model Prediction**  
A trained classifier predicts which gesture is being performed.

### 4️⃣ **Text-to-Speech**  
If the same gesture is detected consistently for several frames:  
✔️ The system **translates the gesture**  
✔️ Speaks the output using **TTS**

---

## 🎯 **Our Mission**

This project is part of our vision to **bridge communication gaps**, especially for:

- People with **hearing disabilities**  
- Individuals with **speech impairments**  
- Children with learning challenges  
- Elderly people who struggle with speech  
- Anyone learning or teaching **Indian Sign Language**

We believe technology should be **inclusive**, **accessible**, and **human-centric**.

---

## 🚧 **Upcoming Features (Stay Tuned!)**

We are actively working on:

🔥 **1. Full Mobile App (Android & iOS)**  
Using Flutter + On-Device MediaPipe + TensorFlow Lite.

🔥 **2. More Gestures (20–50 ISL Signs)**  
Daily-use signs such as:  
- Water  
- Food  
- Help  
- What  
- Where  
- Emergency  

🔥 **3. Two-Hand Gesture Recognition**  
Supporting dual-hand ISL grammar.

🔥 **4. Cloud Model API**  
Allow developers to integrate ISL recognition into apps.

🔥 **5. Offline Mode for Mobile**  
Fast, secure, fully device-side.

We are on a **mission to help the needy**, and your support motivates us to improve!

---

## 🤝 **Contributing**

Pull requests, suggestions, and improvements are welcome!  
You can open issues for:

- Bug reports  
- Feature requests  
- Documentation upgrades  

---

## 🧑‍💻 **Developer**

**Parardha Dhar**  
*Undergraduate CSE Student | ML Enthusiast | Game Developer*  
Working to make technology **more meaningful and accessible.**

---

## ⭐ **Support the Project**

If you like this initiative and want to support accessible technology,  
please **⭐ star the repository** — it really helps!

