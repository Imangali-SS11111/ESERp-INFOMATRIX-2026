SAFE_RESPONSES={
    "phishing": {
        "account verification": "Do not click on any links. Visit the official website manually and check your account status.",
        "credentials theft": "Never share passwords or codes. Legitimate services never ask for them via messages.",
        "security_alert": "Contact the service directly through official support channels.",
        "default": "Avoid interacting with this message and report it as phishing."},
    "financial_manipulation": {
        "prize offer": "Do not forward this message. Legitimate rewards never require message sharing.",
        "investment scam": "Avoid sending money or personal details. Verify offers through official sources.",
        "money refund": "Do not engage. Refunds are processed only through official platforms.",
        "default": "Be cautious of financial offers that pressure you to act."},
    "psychological_pressure": {
        "urgency pressure": "Pause and take time to verify the situation. Urgency is a common manipulation tactic.",
        "authority pressure": "Authorities do not contact individuals via informal messages.",
        "fear inducing": "Stay calm and verify information before taking any action.",
        "default": "Do not act under pressure. Verify independently."},
    "suspicious_commercial": {
        "provocative marketing": "Avoid impulse purchases. Check the seller's legitimacy.",
        "hidden terms": "Read conditions carefully and avoid unclear offers.",
        "fake discount": "Extreme discounts are often misleading. Verify before purchasing.",
        "default": "Be cautious with commercial offers that seem too good to be true." },
    "safe": {
        "default": "No action required. This message appears safe."}}
def safe(category,sub_intent):
    category=category.lower()
    if category not in SAFE_RESPONSES:
        return "While responding be very cautious and tell about this message to your close ones!"
    response=SAFE_RESPONSES[category]
    if sub_intent in response:
        return response[sub_intent]
    return response ["default"]