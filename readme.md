# 🎭 Sentiments Analyser 🌈
A colorful, animated web application for real-time **emotion detection** using **Natural Language Processing (NLP)** powered by a **BERT-based AI model** from Hugging Face.
---
## 🚀 Live Demo

> _Local demo_: Open `http://127.0.0.1:5000` after running `python app.py`

---
## 🔍 Features

- 🎯 Detects emotions like **happy**, **sad**, **anger**, **fear**, **excitement**, and even **horny**
- ⚙️ Powered by **Transformers** from Hugging Face (`bert-base-uncased-emotion`)
- 🎨 Futuristic & colorful animated **frontend UI**
- 🔁 Smooth animations and transitions
- 📦 Fully responsive with **HTML**, **CSS**, and **JavaScript**
- 🔬 Live inference from user input

---

## 🧠 Tech Stack

| Layer        | Tech                             |
|-------------|----------------------------------|
| 🧠 Backend   | Python + Flask + Transformers    |
| 🌐 Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| 📚 ML Model | `nateraw/bert-base-uncased-emotion` |
| 🎨 Design    | Pure CSS animations, particles.js |

---

## ⚙️ How It Works

1. User enters a sentence (e.g., "I love this product!")
2. The frontend sends a **POST** request to `/analyze` with the text
3. The Flask backend passes this to the **emotion detection model**
4. Predicted emotion is mapped to a simpler label and sent back
5. UI displays the result with color and animation

## 📥 Installation & Setup

### 1. Clone the repo
git clone https://github.com/Ayushbadwaik/sentiment-analyser.git.

cd Sentiments-Analyser

2. Install Python dependencies:
pip install flask transformers torch

3. Run the Flask app:
python app.py
Then go to http://127.0.0.1:5000 in your browser.
