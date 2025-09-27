import random

RESPONSES = {
    "happy": [
        "I'm glad you're feeling positive! 🌸 Keep embracing these good moments.",
        "Your happiness is contagious! 💫 Keep spreading that positive energy.",
        "It's wonderful to see you in such high spirits! 🌞"
    ],
    "neutral": [
        "You're taking things in stride, and that's perfectly okay.",
        "Sometimes a calm and neutral perspective helps us see things clearly. 🌿",
        "Balance and patience often guide us through life. 🌼"
    ],
    "sad": [
        "I hear you, and it's okay to feel this way. 🌧️ Remember, emotions pass.",
        "I'm here to listen. You're not alone in this journey. 🤝",
        "Take gentle care of yourself during this time. Your feelings are valid. 💙"
    ],
    "angry": [
        "I understand your frustration. Let's take a deep breath together. 🌬️",
        "Your feelings are valid. Would you like to share more about what's bothering you?",
        "It's okay to feel angry. Anger often points to something important. ❤️"
    ],
    "anxious": [
        "Anxiety can feel heavy, but you're stronger than you think. 💪",
        "Try grounding yourself with a deep breath. You're safe right now. 🌱",
        "Worries come and go, but your inner calm remains. 🕊️"
    ],
    "stressed": [
        "I know things feel overwhelming. Remember to pause and rest. 🌸",
        "You're carrying a lot. It's okay to set boundaries for your peace. 🌙",
        "Take things one step at a time—you’re doing your best. 🌈"
    ],
    "fearful": [
        "Fear can feel strong, but it doesn’t define you. 🌟",
        "You're safe in this moment. Trust yourself, you're resilient. 🌿",
        "It's okay to feel afraid. Let’s face this together with courage. 💜"
    ],
    "tired": [
        "Rest is important. You deserve to recharge. 😴",
        "It's okay to slow down. Listen to what your body and mind need. 🌙",
        "Take a break—you’ve earned it. 🌼"
    ],
    "hopeful": [
        "I love the hope you're carrying—hold on to it. 🌅",
        "Even small steps forward matter. Keep going. 🌟",
        "Hope is a powerful light. Let it guide you. ✨"
    ],
    "grateful": [
        "Gratitude is such a healing force. Thank you for sharing yours. 🌸",
        "Acknowledging the good in life strengthens us. 💖",
        "Your gratitude shines through—it’s inspiring. 🌞"
    ]
}

def generate_response(emotion, user_input=None, deterministic=False):
    """Generate a supportive response based on detected emotion"""
    responses = RESPONSES.get(emotion, [
        "I'm here to listen and support you. 💙",
        "Thank you for sharing your feelings with me. 🤗",
        "Would you like to tell me more about how you're feeling?"
    ])
    response = responses[0] if deterministic else random.choice(responses)
    
    if user_input:
        response += f" I hear you said: '{user_input}'."
    
    return response
