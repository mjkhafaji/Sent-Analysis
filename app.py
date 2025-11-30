from flask import Flask, request, jsonify
from logic import analyze_mood  # Import your AI brain

app = Flask(__name__)

@app.route("/")
def home():
    return "The AI Sentiment Server is Running!"

@app.route("/analyze", methods=['POST'])
def analyze():
    # 1. Get the text sent by the user
    data = request.get_json()
    user_text = data.get('text', '')

    # 2. Pass it to your AI brain
    result = analyze_mood(user_text)

    # 3. Return the result as JSON
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)