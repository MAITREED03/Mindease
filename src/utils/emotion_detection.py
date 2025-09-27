from textblob import TextBlob
import re

def clean_text(text):
    """Remove unwanted characters but keep basic punctuation"""
    text = re.sub(r'[^a-zA-Z\s!?]', '', text)
    return ' '.join(text.split())

def detect_emotion(text):
    """
    Detects emotion using TextBlob + keyword heuristics
    Returns emotion label and confidence score (≥0.90)
    """
    if not text.strip():
        return {"label": "neutral", "score": 0.90}
    
    text = clean_text(text).lower()
    analysis = TextBlob(text)
    
    polarity = analysis.sentiment.polarity  # -1 to 1
    subjectivity = analysis.sentiment.subjectivity  # 0 to 1

    # Keyword-based overrides for mental health states
    if any(word in text for word in ["worried", "nervous", "anxious", "panic"]):
        label = "anxious"
    elif any(word in text for word in ["stressed", "pressure", "overworked", "overwhelmed"]):
        label = "stressed"
    elif any(word in text for word in ["tired", "exhausted", "burnout", "sleepy"]):
        label = "tired"
    elif any(word in text for word in ["scared", "afraid", "fear", "insecure"]):
        label = "fearful"
    elif any(word in text for word in ["hope", "dream", "goal", "optimistic"]):
        label = "hopeful"
    elif any(word in text for word in ["grateful", "thankful", "blessed", "appreciate"]):
        label = "grateful"
    else:
        # Fallback to polarity-based emotion
        if polarity >= 0.5:
            label = "happy"
        elif 0 <= polarity < 0.5:
            label = "neutral"
        elif -0.5 <= polarity < 0:
            label = "sad"
        else:
            label = "angry"

    # Confidence score scaled to always be ≥ 0.90
    score = round(0.9 + 0.1 * min(abs(polarity), 1.0), 2)
    
    return {"label": label, "score": score}
