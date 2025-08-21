import random

def emotion_detector(text_to_analyze):
    """
    Version simulée de l'analyse d'émotion pour usage hors ligne.
    Renvoie des scores aléatoires pour chaque émotion et la dominante.
    """
    # Scores d'émotions simulés (entre 0 et 1)
    anger_score = round(random.uniform(0, 1), 2)
    disgust_score = round(random.uniform(0, 1), 2)
    fear_score = round(random.uniform(0, 1), 2)
    joy_score = round(random.uniform(0, 1), 2)
    sadness_score = round(random.uniform(0, 1), 2)

    # Dictionnaire complet des scores
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    # Émotion dominante
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "text": text_to_analyze,
        "emotions": emotion_scores,
        "dominant_emotion": dominant_emotion
    }

# Test rapide (optionnel, pour shell Python)
if __name__ == "__main__":
    sample_text = "I love this new technology."
    print(emotion_detector(sample_text))
