from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/emotionDetector")
def text_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection.emotion_detector(text_to_analyze)

    # Check for error in response
    if "error" in response:
        return "Error: " + response["error"]

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['label']

    return ("For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy}, 'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
