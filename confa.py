def calculate_confidence(model, message, triggers, risk_score):
    proba = max(model.predict_proba([message])[0])
    trigger_bonus = min(len(triggers) * 0.1, 0.3)
    risk = risk_score / 100
    confidence = (proba + trigger_bonus) * risk
    return round(min(confidence, 1.0), 2)
