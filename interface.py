import streamlit as st
from explanation import generate_explanation
from risk import calculate_risk_score
from subintents import detect_subintent
from triggers import detect_trigger_words
from confa import calculate_confidence
from trajectory import analyze_trajectory
from safe_response import safe
import joblib

model = joblib.load("model.pkl")

st.set_page_config(page_title="Threat Analysis Demo", layout="centered")

st.title("Message Threat Analysis System")
st.write("Enter a message to analyze potential risks, intent, and safety recommendations.")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

message = st.text_area("Input message")

if st.button("Analyze") and message:
    category = model.predict([message])[0]
    st.session_state.conversation.append(category)

    sub_intent = detect_subintent(message, category)
    triggers = detect_trigger_words(message)
    risk_score = calculate_risk_score(category, message)
    trajectory = analyze_trajectory(st.session_state.conversation)
    explanation = generate_explanation(category, message) + " " + trajectory["trajectory_explanation"]
    final_risk = min(risk_score + trajectory["trajectory_risk"], 100)
    safe_responses=safe(category,sub_intent)
    confidence = calculate_confidence(model, message, triggers, risk_score)
    

    st.subheader("Analysis Result")
    st.write("**Category:**", category)
    st.write("**Sub-intent:**", sub_intent)
    st.write("**Risk score:**", final_risk)
    st.write("**System confidence:**", round(confidence, 2))
    st.write("**Trigger words:**", triggers)
    st.write("**Explanation:**", explanation)
    st.write("**Suggested response:**",safe_responses)

    if final_risk >= 70:
        st.error("High risk detected. Do not interact with this message.")
    elif final_risk >= 30:
        st.warning("Medium risk. Verify before taking action.")
    else:
        st.success("Low risk. Message appears safe.")
