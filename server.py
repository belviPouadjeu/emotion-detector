from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")

# ✅ Nouvelle route GET demandée par le projet
@app.route("/emotionDetector")
def emotion_detector_route():
    text = request.args.get("textToAnalyze", "")
    result = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"
    else:
        return (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

# Route POST (si tu veux utiliser AJAX dans index.html)
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    result = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
