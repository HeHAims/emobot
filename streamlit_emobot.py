import streamlit as st
from core.assistant import EmoBot
from core.math_translator import EnhancedMathTranslator
from core.memory import Memory
from core.emotions import EmotionEngine
from core.self_model import SelfModel
from core.goal_system import GoalSystem

# Initialize EmoBot components if not already in session
if 'emo_bot' not in st.session_state:
    memory = Memory(capacity=1000)
    emotions = EmotionEngine()
    goals = GoalSystem()
    self_model = SelfModel()
    translator = EnhancedMathTranslator()
    st.session_state.emo_bot = EmoBot(memory, emotions, goals, self_model, translator)

st.title("🤖 EmoBot - The Emotional Math Tutor")

# User input
user_input = st.text_input("Enter a math formula:", "")

if user_input:
    response = st.session_state.emo_bot.explain_formula(user_input)
    st.write(response)

    feedback = st.text_input("Your feedback:", "")
    if feedback:
        # Check if feedback is a new formula
        if any(c.isalpha() for c in feedback) and any(sym in feedback for sym in "+-*/=^∫∂Σ()"):
            response = st.session_state.emo_bot.explain_formula(feedback)
        else:
            response = st.session_state.emo_bot.handle_user_feedback(feedback)
        st.write(response)
