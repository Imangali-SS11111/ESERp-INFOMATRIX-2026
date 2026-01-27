def calculate_risk_score(category, text):
    base_scores = {
        "phishing": 90,
        "financial_manipulation": 75,
        "psychological_pressure": 65,
        "suspicious_commercial": 50,
        "safe": 5}
    score=base_scores.get(category,30)
    text_lower=text.lower()
    if "http" in text_lower or "www" in text_lower:
        score += 5
    if "urgent" in text_lower or "immediately" in text_lower:
        score += 5
    if "password" in text_lower or "account" in text_lower:
        score += 10

    return min(score, 100)
