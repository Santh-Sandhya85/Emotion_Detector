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

# import requests
#
# def emotion_detector(text_to_analyze):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {
#         "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
#     }
#     input_json = {
#         "raw_document": {
#             "text": text_to_analyze
#         }
#     }
#
#     try:
#         # Disable SSL verification for testing
#         response = requests.post(url, headers=headers, json=input_json, verify=False)
#         response.raise_for_status()  # Raise an error for bad responses
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")
#         return None
#
# # Test the function
# result = emotion_detector("I love this new technology.")
# print(result)







# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#
#
# def emotion_predictor(text):
#     authenticator = IAMAuthenticator('your_api_key')  # Replace with your API key
#     nlu = NaturalLanguageUnderstandingV1(
#         version='2021-08-01',
#         authenticator=authenticator
#     )
#     nlu.set_service_url('http://your_service_url')  # Replace with your service URL
#
#     response = nlu.analyze(
#         text=text,
#         features=Features(emotion=EmotionOptions())
#     ).get_result()
#     # Format the output
#     emotions = response['emotion']['document']['emotion']
#     formatted_output = {emotion: round(score * 100, 2) for emotion, score in emotions.items()}
#     return formatted_output
#     # return response

# Mocked function to simulate emotion detection
# def emotion_predictor(text):
#     # Mock response simulating what would come from the Watson NLU API
#     mock_response = {
#         "emotion": {
#             "document": {
#                 "emotion": {
#                     "joy": 0.85,
#                     "anger": 0.05,
#                     "sadness": 0.02,
#                     "fear": 0.03,
#                     "disgust": 0.05
#                 }
#             }
#         }
#     }
#
#     # Return the mock response instead of calling the actual API
#     return mock_response
#

# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# def emotion_predictor(text):
#
#     authenticator = IAMAuthenticator('your_api_key')
#     nlu = NaturalLanguageUnderstandingV1(
#         version='2021-08-01',
#         authenticator=authenticator
#     )
#     nlu.set_service_url('your_service_url')
#
#     response = nlu.analyze(
#         text=text,
#         features=Features(emotion=EmotionOptions())
#     ).get_result()
#
#     # Format the output
#     emotions = response['emotion']['document']['emotion']
#     formatted_output = {emotion: round(score * 100, 2) for emotion, score in emotions.items()}
#     return formatted_output


# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# def emotion_predictor(text):
#
#     authenticator = IAMAuthenticator('your_api_key')
#     nlu = NaturalLanguageUnderstandingV1(
#         version='2021-08-01',
#         authenticator=authenticator
#     )
#     nlu.set_service_url('your_service_url')
#
#     response = nlu.analyze(
#         text=text,
#         features=Features(emotion=EmotionOptions())
#     ).get_result()
#
#     # Format the output
#     emotions = response['emotion']['document']['emotion']
#     formatted_output = {emotion: round(score * 100, 2) for emotion, score in emotions.items()}
#
#     # Return the formatted output
#     return formatted_output

# import requests
# import logging
#
# logging.basicConfig(level=logging.DEBUG)
#
#
# def emotion_detector(text_to_analyze):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     input_json = {"raw_document": {"text": text_to_analyze}}
#
#     try:
#         response = requests.post(url, headers=headers, json=input_json)
#         response.raise_for_status()
#         return response.json().get('text', 'No emotion detected')
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Request failed: {e}")
#         return f"An error occurred: {e}"

# import requests
#
# def test_emotion_detector():
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     input_json = {"raw_document": {"text": "Test"}}
#
#     try:
#         response = requests.post(url, headers=headers, json=input_json)
#         response.raise_for_status()
#         print(response.json())
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#
#
# test_emotion_detector()






