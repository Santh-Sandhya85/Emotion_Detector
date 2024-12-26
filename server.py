"""
server.py - A Flask application for emotion detection.

This module contains the Flask application routes for processing
user input and returning detected emotions.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Process the input text and return the detected emotions.

    Returns:
        str: A message containing the emotion analysis results or an error message.
    """
    data = request.json
    text_to_analyze = data.get('text', '')

    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        if result and result['dominant_emotion'] is not None:
            response_message = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )
            return response_message, 200

    return "Invalid text! Please try again!", 400  # Handle blank entries or invalid input

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
