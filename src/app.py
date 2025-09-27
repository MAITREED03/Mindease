import streamlit as st
from utils.emotion_detection import detect_emotion
from utils.responder import generate_response
from PIL import Image
import pandas as pd
import os
from datetime import datetime

# --- UI Setup ---
st.set_page_config(
    page_title="MindEase: Your AI Mental Health Companion",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stTextArea > label { font-size: 20px; }
    .stButton > button { width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Logo
try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=120)
except:
    st.title("🧠 MindEase")

st.subheader("Your AI Mental Health Companion")
st.markdown("---")

# Emoji map for emotions
EMOJI_MAP = {
    "happy": "😊",
    "neutral": "😐",
    "sad": "😢",
    "angry": "😡",
    "anxious": "😟",
    "stressed": "😩",
    "fearful": "😨",
    "tired": "🥱",
    "hopeful": "🌅",
    "grateful": "🙏"
}

# Path for journaling
JOURNAL_FILE = "journal.csv"

# --- Emotion Analysis Section ---
user_input = st.text_area("How are you feeling today? 💭", height=150)

if st.button("Analyze Emotion 🔍"):
    if user_input.strip():
        with st.spinner("Analyzing your emotions..."):
            result = detect_emotion(user_input)
            emotion = result["label"]
            score = result["score"]

            # Display results
            st.markdown(f"### 🎭 Detected Emotion: **{emotion.title()} {EMOJI_MAP.get(emotion, '')}**")
            st.markdown(f"### 📊 Confidence: **{score * 100:.0f}%**")
            st.progress(score)

            st.markdown("---")
            st.markdown("### 💡 MindEase's Response:")
            st.success(generate_response(emotion, user_input))

            # Save to journal (analyzed entry)
            entry = {
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": "analyzed",
                "emotion": emotion,
                "confidence": f"{score * 100:.0f}%",
                "text": user_input
            }

            if os.path.exists(JOURNAL_FILE):
                df = pd.read_csv(JOURNAL_FILE)
                df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
            else:
                df = pd.DataFrame([entry])
            df.to_csv(JOURNAL_FILE, index=False)

            st.success("📝 Your analyzed entry has been added to your journal.")
    else:
        st.warning("Please share your thoughts so I can help you better.")

# --- Free Journaling Section ---
st.markdown("---")
st.markdown("## ✍️ Journal Your Thoughts (Free Writing)")

free_entry = st.text_area(
    "Write freely about what's on your mind, without any analysis. "
    "This is your personal space to reflect, vent, or dream. 🌿",
    height=200
)

if st.button("Save Journal Entry 📖"):
    if free_entry.strip():
        entry = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": "free",
            "emotion": "-",  # no emotion detection here
            "confidence": "-",
            "text": free_entry
        }

        if os.path.exists(JOURNAL_FILE):
            df = pd.read_csv(JOURNAL_FILE)
            df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
        else:
            df = pd.DataFrame([entry])
        df.to_csv(JOURNAL_FILE, index=False)

        st.success("📓 Your free journal entry has been saved.")
    else:
        st.warning("Please write something before saving.")

# --- Show Journal ---
st.markdown("---")
st.markdown("### 📖 Your Journal (Recent Entries)")
if os.path.exists(JOURNAL_FILE):
    df = pd.read_csv(JOURNAL_FILE)
    st.dataframe(df.tail(10), use_container_width=True)
    if st.download_button("⬇️ Download Full Journal", df.to_csv(index=False), "journal.csv"):
        st.success("Your journal has been downloaded.")
else:
    st.info("No journal entries yet. Start by sharing your thoughts above!")
