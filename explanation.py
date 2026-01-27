def generate_explanation(category, text):
    text_lower = text.lower()

    EXPLANATIONS = {
        "phishing": [
            {"keywords": ["login", "password", "account"],"text": "This message impersonates a trusted service to trick the user into revealing sensitive information."},
            {"keywords": ["verify", "confirm"],"text": "The message requests account verification, which is a common phishing technique."},
            {"keywords": ["suspended", "blocked", "security"],"text": "The sender creates a fake security alert to pressure the user into acting quickly."},
            {"keywords": [],"text": "This is a phishing attempt designed to steal personal or login data."}],

        "financial_manipulation": [
            {"keywords": ["money", "$", "reward", "paid"],"text": "This message offers a financial reward to influence the user's behavior."},
            {"keywords": ["invest", "profit", "guaranteed"],"text": "The sender promotes financial gain as a manipulation tactic."},
            {"keywords": [],"text": "This is a financial manipulation attempt exploiting greed or curiosity."}],

        "psychological_pressure": [
            {"keywords": ["urgent", "immediately", "now"],"text": "This message creates urgency to push the user into acting without careful thinking."},
            {"keywords": ["legal", "police", "bank"],"text": "The sender applies authority pressure to reduce rational decision-making."},
            {"keywords": [] ,"text": "Fear or stress is used here as a psychological manipulation technique."}],

        "suspicious_commercial": [
            {"keywords": ["buy", "offer", "discount"],"text": "This message promotes a commercial offer in a suspicious and unsolicited manner." },
            {"keywords": [],"text": "The commercial content lacks transparency and verifiable details."}],

        "safe": [
            { "keywords": [],"text": "This message does not show signs of manipulation or malicious intent."}]}

    templates = EXPLANATIONS.get(category)
    if not templates:
        return "No explanation available."

    for template in templates:
        for kw in template["keywords"]:
            if kw in text_lower:
                explanation = template["text"]
                break
        else:
            continue
        break
    else:
        explanation = templates[0]["text"]

    return explanation
