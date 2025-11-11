# chatbot_logic.py
from nltk.chat.util import Chat, reflections
from google_search import google_search  # Import the search function

pairs = [
    ["hi|hello", ["Hello! How can I help you today?"]],
    ["what is your name?", ["I'm Iris, your support assistant."]],
    ["what is your gender?", ["I'm Technically male assistant."]],
    ["how to reset password?", ["Click 'Forgot Password' on the login page."]],
    ["bye", ["Goodbye! Have a great day."]],
]

def get_response(user_input):
    chatbot = Chat(pairs, reflections)
    response = chatbot.respond(user_input)
    if response is None:
        web_answer = google_search(user_input)
        return "WEB: " + web_answer
    return response

