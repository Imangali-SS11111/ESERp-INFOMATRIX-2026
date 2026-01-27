Sub_intent={"phishing":{
        "account verification":["login", "password", "verify", "sign in"],
        "credentials theft":["suspicious activity", "account locked"],
        "security_alert":["confirm your account", "verify account"]},
    "financial_manipulation":{
        "prize offer":["won", "prize", "reward", "gift","money"],
        "investment scam":["invest", "profit", "guaranteed"],
        "Money refund":["refund", "return money"]},
    "psychological_pressure":{
        "urgency pressure":["urgent", "immediately", "24 hours"],
        "authority pressure":["police", "bank", "government"],
        "fear inducing":["suspended", "blocked", "legal action"]},
    "suspiciuos_commercial":{
        "provocative marketing":["limited offer", "buy now", "only today"],
        "hidden terms":["conditions apply", "small print"],
        "fake discount":["huge discount", "90% off"]}}
def detect_subintent(text,category):
    text=text.lower()
    if category not in Sub_intent:
        return None
    for sub_intent,keywords in Sub_intent[category].items():
        for word in keywords:
            if word in text:
                return sub_intent

