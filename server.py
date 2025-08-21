from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Vérifie que le package est correct

app = Flask(__name__, template_folder="templates", static_folder="static")

# Page d'accueil
@app.route("/")
def home():
    return render_template("index.html")

# Route POST pour analyser le texte (depuis JS)
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    result = emotion_detector(text)

    if "dominant_emotion" in result:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    else:
        response_text = f"Error: {result.get('error', 'Unknown error')}"

    return jsonify({"response": response_text})

# Route GET pour permettre l'accès direct via navigateur
@app.route("/emotionDetector")
def emotion_detector_get():
    text = request.args.get("textToAnalyze", "")
    result = emotion_detector(text)

    if "dominant_emotion" in result:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
    else:
        response_text = f"Error: {result.get('error', 'Unknown error')}"

    return response_text

if __name__ == "__main__":
    app.run(debug=True)

