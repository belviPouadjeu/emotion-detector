import requests
import json

def emotion_detector(text_to_analyze):
    """
    Envoie le texte à l'API Watson NLP pour détecter les émotions.
    En cas de problème de connexion, retourne un résultat simulé.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        # Timeout 10s pour éviter les blocages
        response = requests.post(url, headers=headers, json=input_json, timeout=10)

        if response.status_code == 200:
            # Requête réussie, récupérer le JSON
            response_dict = response.json()

            # Extraire les émotions
            emotions = response_dict['emotionPredictions'][0]['emotion']
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Trouver l’émotion dominante
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Retourner le résultat complet
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion,
                'text': text_to_analyze
            }

        else:
            return {"error": f"Request failed with status {response.status_code}", "text": text_to_analyze}

    except requests.exceptions.ConnectTimeout:
        return {"error": "Connection timed out. The Watson API may be unreachable.", "text": text_to_analyze}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}", "text": text_to_analyze}


# -----------------------
# Test rapide depuis le Python shell
# -----------------------
if __name__ == "__main__":
    text_to_analyze = "I love this new technology."
    result = emotion_detector(text_to_analyze)
    print("Texte analysé :", text_to_analyze)
    print("Résultat de l'analyse d'émotion :")
    print(result)
