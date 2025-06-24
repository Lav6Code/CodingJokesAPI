from flask import Flask, jsonify, request
import os, random

app = Flask(__name__)

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "Debugging: being the detective in a crime movie where you’re also the murderer.",
    # ... more jokes ...
]

@app.route("/joke")
def joke():
    api_key = request.headers.get("X-RapidAPI-Key")
    allowed_key = os.getenv("RAPIDAPI_KEY")

    if api_key != allowed_key:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"joke": random.choice(jokes)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
