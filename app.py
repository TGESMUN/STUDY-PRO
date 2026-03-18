from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")
        q4 = request.form.get("q4")
        q5 = request.form.get("q5")
        q6 = request.form.get("q6")
        q7 = request.form.get("q7")
        q8 = request.form.get("q8")
        q9 = request.form.get("q9")
        q10 = request.form.get("q10")

        score = 0

        if q1 == "night":
            score += 2
        if q2 == "yes":
            score += 2
        if q3 == "no":
            score += 1
        if q4 == "yes":
            score += 2
        if q5 == "short":
            score += 1
        if q6 == "music":
            score += 1
        if q7 == "visual":
            score += 1
        if q8 == "late":
            score += 2
        if q9 == "alone":
            score += 1
        if q10 == "planner":
            score -= 1

        if score >= 8:
            result = {
                "title": "🔥 Focus Sprinter",
                "description": "You work in intense bursts and often rely on pressure to perform.",
                "tips": [
                    "Use Pomodoro: 25 min focus + 5 min break",
                    "Keep your phone away while studying",
                    "Set mini deadlines before the real deadline",
                    "Use timers to maintain urgency"
                ],
                "color": "#ff5f6d"
            }
        elif score >= 4:
            result = {
                "title": "⚡ Adaptive Learner",
                "description": "You’re flexible and can perform well in different situations, but consistency will make you stronger.",
                "tips": [
                    "Follow a simple study routine every day",
                    "Mix short revision with deep study sessions",
                    "Track daily progress in a checklist",
                    "Study hard subjects during your peak energy hours"
                ],
                "color": "#4facfe"
            }
        else:
            result = {
                "title": "🌱 Calm Planner",
                "description": "You prefer stability, routine, and steady progress over pressure.",
                "tips": [
                    "Create a fixed weekly timetable",
                    "Study in calm, distraction-free spaces",
                    "Revise a little every day",
                    "Use written plans to stay motivated"
                ],
                "color": "#43e97b"
            }

    return render_template("index.html", result=result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)