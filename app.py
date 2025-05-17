from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load Hugging Face pipeline for emotion classification
emotion_classifier = pipeline("text-classification", model="nateraw/bert-base-uncased-emotion", return_all_scores=False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"sentiment": "neutral"})

    # Run the emotion classifier pipeline
    result = emotion_classifier(text[:512])  # limit input size for performance

    # Result example: [{'label': 'joy', 'score': 0.99}]
    emotion = result[0]['label']

    # Map Huggingface emotions to your custom set
    map_emotion = {
        "joy": "happy",
        "sadness": "sad",
        "anger": "anger",
        "fear": "fear",
        "love": "horny",
        "surprise": "excitement"
    }
    mapped_emotion = map_emotion.get(emotion, "neutral")

    return jsonify({"sentiment": mapped_emotion})

if __name__ == "__main__":
    app.run(debug=True)
