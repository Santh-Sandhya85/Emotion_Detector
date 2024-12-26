import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        print("Sending request to Watson NLP...")
        print(f"URL: {url}")
        print(f"Headers: {headers}")
        print(f"Input JSON: {input_json}")

        response = requests.post(url, headers=headers, json=input_json, verify=False)
        response.raise_for_status()  # Raise an error for bad responses

        # Print the raw response for debugging
        print("Response received:", response.json())

        data = response.json()

        # Extract emotion scores
        anger_score = data.get('emotion', {}).get('anger', 0)
        disgust_score = data.get('emotion', {}).get('disgust', 0)
        fear_score = data.get('emotion', {}).get('fear', 0)
        joy_score = data.get('emotion', {}).get('joy', 0)
        sadness_score = data.get('emotion', {}).get('sadness', 0)

        # Create the output dictionary
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
        }

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Add the dominant emotion to the output
        emotions['dominant_emotion'] = dominant_emotion

        return emotions

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

