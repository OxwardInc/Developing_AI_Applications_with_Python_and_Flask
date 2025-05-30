import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # raises error for HTTP codes 4xx/5xx
        formatted_response = response.json()

        # Extract the emotion scores
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['label'] = dominant_emotion

        return emotions

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
    except (KeyError, IndexError, ValueError) as e:
        return {"error": f"Error parsing response: {e}"}