# app.py
from flask import Flask, render_template, request
from chatbot_logic import get_response
from database import log_interaction

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    bot_reply = get_response(user_input)
    log_interaction(user_input, bot_reply)
    return bot_reply

if __name__ == "__main__":
    app.run(debug=True)
