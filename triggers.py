TRIGGER_WORDS = {
    "phishing": [
        "login", "password", "verify", "account", "confirm",
        "sign in", "suspended", "security alert"],
    "financial_manipulation": [
        "money", "reward", "prize", "won", "gift",
        "investment", "profit", "guaranteed", "refund"],
    "psychological_pressure": [
        "urgent", "immediately", "act now", "24 hours",
        "final warning", "legal action"],
    "suspicious_commercial": [
        "buy now", "limited offer", "only today",
        "huge discount", "90% off", "free trial"]}

def detect_trigger_words(text):
    text = text.lower()
    detected = []

    for category, words in TRIGGER_WORDS.items():
        for word in words:
            if word in text:
                detected.append(word)

    return list(set(detected))
