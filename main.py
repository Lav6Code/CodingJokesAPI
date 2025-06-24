from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/joke")
def joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
        "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
        "What do you call 8 hobbits? A hobbyte.",
        "Why did the Python programmer get rejected? Because he had too many `self` issues.",
        "There are only 10 types of people in the world: those who understand binary and those who don’t.",
        "Debugging: Being the detective in a crime movie where you are also the murderer.",
        "Why are assembly programmers always soaking wet? They work below C-level.",
        "Why did the computer show up at work late? It had a hard drive.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why did the software engineer cross the road? To get to the other IDE.",
        "Why did the developer become a gardener? To learn about branching.",
        "The best thing about a boolean is even if you are wrong, you are only off by a bit.",
        "Writing code is like humor: if you have to explain it, it’s bad."
    ]

    return jsonify({"joke": random.choice(jokes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
