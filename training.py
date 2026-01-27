import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from explanation import generate_explanation
from risk import calculate_risk_score
from trajectory import analyze_trajectory
from subintents import detect_subintent
from safe_response import safe
from triggers import detect_trigger_words
from confa import calculate_confidence


data = pd.read_csv("dataset.csv")

X = data["message"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

test_messages = [
    "We offer you money if you forward this message",
    "Hi, how are you?",
    "Urgent response required",
    "Your account is under review. Login required to proceed."]

conversation_category = []

for msg in test_messages:
    predicted_category = model.predict([msg])[0]
    conversation_category.append(predicted_category)
    sub_intent = detect_subintent(msg,predicted_category)
    safe_responses=safe(predicted_category,sub_intent)
    triggers = detect_trigger_words(msg)
    risk_score = calculate_risk_score(predicted_category, msg)
    confidence = calculate_confidence(model, msg, triggers,risk_score)

    trajectory_result = analyze_trajectory(conversation_category)
    trajectory_risk = trajectory_result["trajectory_risk"]
    trajectory_explanation = trajectory_result["trajectory_explanation"]
    final_risk = min(risk_score + trajectory_risk, 100)

    full_explanation = generate_explanation(predicted_category, msg) + " " + trajectory_explanation
    print("Message:",msg)
    print("Category:", predicted_category)
    print("Sub intent:",sub_intent)
    print("Risk score:", final_risk, "/100")
    print("Triggers:", triggers)
    print("System confidence:", confidence)
    print("Explanation:", full_explanation)
    print("Suggested response:",safe_responses)
    joblib.dump(model,"model.pkl")




