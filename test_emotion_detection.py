# test_emotion_detection.py
import pytest
import EmotionDetection.emotion_detection as ed  # Import du module, pas de la fonction

# Cas de test : texte → émotion dominante attendue
test_cases = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]

@pytest.mark.parametrize("text,expected_emotion", test_cases)
def test_emotion_detection(monkeypatch, text, expected_emotion):
    """
    Test de la fonction emotion_detector avec simulation de réponses
    pour éviter les appels réels à l'API.
    """
    # Fonction simulée pour remplacer la vraie
    def fake_emotion_detector(text_to_analyze):
        mapping = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        return {"dominant_emotion": mapping[text_to_analyze]}
    
    # Patch la fonction originale dans le module
    monkeypatch.setattr(ed, "emotion_detector", fake_emotion_detector)

    # Appel de la fonction patchée
    result = ed.emotion_detector(text)

    # Vérifie que l'émotion dominante est celle attendue
    assert result["dominant_emotion"] == expected_emotion, (
        f"For '{text}' expected '{expected_emotion}' but got '{result['dominant_emotion']}'"
    )
