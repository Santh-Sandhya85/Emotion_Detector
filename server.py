
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    data = request.json
    text_to_analyze = data.get('text', '')
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        if result:
            response_message = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
            )
            return response_message, 200
        else:
            return "Emotion detection failed.", 500
    else:
        return "No text is provided.", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
