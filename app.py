from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    success = False

    if request.method == "POST":
        message_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "company": request.form.get("company"),
            "message": request.form.get("message"),
            "date": datetime.now().strftime("%d.%m.%Y %H:%M")
        }

        try:
            with open("messages.json", "r", encoding="utf-8") as file:
                messages = json.load(file)
        except FileNotFoundError:
            messages = []

        messages.append(message_data)

        with open("messages.json", "w", encoding="utf-8") as file:
            json.dump(messages, file, ensure_ascii=False, indent=4)

        success = True

    return render_template("index.html", success=success)

    
@app.route("/cv")
def cv():
    return render_template("cv.html")

if __name__ == "__main__":
    app.run(debug=True)

