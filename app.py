from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    status = ""
    risk = ""
    reasons = []

    ip = ""
    browser = ""
    current_time = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        ip = request.remote_addr

        browser = request.user_agent.browser

        if browser is None:
            browser = "Unknown Browser"

        current_time = datetime.now().strftime("%d %b %Y | %I:%M %p")

        suspicious = False

        if len(password) < 8:
            suspicious = True
            reasons.append("Password is too short.")

        if not any(c.isupper() for c in password):
            suspicious = True
            reasons.append("No uppercase letter detected.")

        if not any(c.isdigit() for c in password):
            suspicious = True
            reasons.append("No numeric value detected.")

        if ip.startswith("127."):

            reasons.append("Running on Localhost.")

        elif ip.startswith("192.168."):

            reasons.append("Login from Local Network.")

        else:

            suspicious = True
            reasons.append("Unknown Network.")

        if suspicious:

            status = "Suspicious Login"

            risk = "High"

        else:

            status = "Safe Login"

            risk = "Low"

    return render_template(

        "index.html",

        status=status,

        risk=risk,

        reasons=reasons,

        ip=ip,

        browser=browser,

        current_time=current_time

    )

if __name__ == "__main__":
    app.run(debug=True)