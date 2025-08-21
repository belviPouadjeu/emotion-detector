import random

def emotion_detector(text_to_analyze):
    """
    Version simulée pour formatage des émotions.
    Retourne un dictionnaire avec :
    - les scores pour anger, disgust, fear, joy, sadness
    - l'émotion dominante
    """
    # Valeurs simulées
    anger_score = round(random.uniform(0, 1), 2)
    disgust_score = round(random.uniform(0, 1), 2)
    fear_score = round(random.uniform(0, 1), 2)
    joy_score = round(random.uniform(0.8, 1), 2)  # forcer la joie dominante
    sadness_score = round(random.uniform(0, 0.5), 2)

    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Déterminer l'émotion dominante
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    return emotions
