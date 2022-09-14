from flask import Flask, render_template, request
import smtplib
app = Flask(__name__)
my_email = "pnikola900@gmail.com"
my_pass = "epopfdljtgnbyirk"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    number = request.form["phone-number"]
    send_email(name, email, number)
    return render_template('index.html')


def send_email(name, email, phone):
    email_message = f"Subject:Proba\n\nIme: {name}\nEmail: {email}\nBroj telefona: {phone}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="pnikola600@gmail.com", msg=email_message)