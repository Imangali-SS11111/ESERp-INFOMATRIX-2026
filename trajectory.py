INTENT_ORDER = {
    "safe": 0,
    "suspicious_commercial": 1,
    "psychological_pressure": 2,
    "financial_manipulation": 3,
    "phishing": 4}
def analyze_trajectory(intents):
    scores=[]
    for i in intents:
        score=INTENT_ORDER.get(i,0)
    scores.append(score)
    delta=scores[-1]-scores[0]
    if delta >= 2:
        return{
    "trajectory_risk": 20,
    "trajectory_explanation": "Escalating malicious intent detected"}
    return {
    "trajectory_risk": 0,
    "trajectory_explanation": "No escalation detected"}
