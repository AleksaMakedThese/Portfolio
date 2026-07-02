from flask import Flask, render_template, request
import resend
import json
from datetime import datetime
import os

app = Flask(__name__)

resend.api_key = os.environ.get("RESEND_API_KEY")


@app.route("/", methods=["GET", "POST"])
def index():
    success = False

    if request.method == "POST":
        message_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "company": request.form.get("company"),
            "message": request.form.get("message"),
            "date": datetime.now().strftime("%d.%m.%Y %H:%M"),
        }

        resend.Emails.send({
            "from": "Portfolio <onboarding@resend.dev>",
            "to": ["och.nrw@gmail.com"],
            "subject": "Neue Nachricht von Portfolio",
            "reply_to": message_data["email"],
            "text": f"""
Name: {message_data["name"]}

E-Mail: {message_data["email"]}

Firma: {message_data["company"]}

Nachricht:

{message_data["message"]}

Gesendet am:
{message_data["date"]}
"""
        })

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

    @media (max-width: 700px) {

    /* 1. Hero: дать фото и тексту нормальное расстояние */
    .hero-content {
        display: flex;
        flex-direction: column;
        gap: 36px;
        padding: 0 24px;
        margin-top: 60px;
    }

    .hero-image-area {
        min-height: auto;
        margin-top: 20px;
    }

    .profile-image {
        width: 280px;
        height: 280px;
    }

    .hero-image-area::before {
        width: 340px;
        height: 160px;
        transform: translate(-50%, -45%);
    }


    /* 2. Skills: все круги в один горизонтальный ряд */
    .grid {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 18px;
        padding-bottom: 16px;
        justify-content: flex-start;
    }

    .skill-card {
        flex: 0 0 170px;
        width: 170px;
        height: 170px;
    }


    /* 3. CV: поднять floating box выше */
    .floating-cta {
        position: fixed;
        left: auto;
        right: 24px;
        bottom: 90px;
        width: 210px;
    }
}