from flask import Flask, render_template, request
import random

app = Flask(__name__)

# File to store best time
BEST_TIME_FILE = "best_time.txt"


@app.route("/")
def index():
    # Greek symbols for cards
    symbols = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ']

    # Get level from URL (default = 12)
    level = request.args.get('level', default=12, type=int)

    # Each symbol needs a pair
    num_pairs = level // 2

    selected_symbols = symbols[:num_pairs] * 2
    random.shuffle(selected_symbols)

    # Read best time from file
    with open(BEST_TIME_FILE, "r") as f:
        best_time = f.read()

    return render_template(
        "index.html",
        cards=selected_symbols,
        best_time=best_time
    )


@app.route("/save_time", methods=["POST"])
def save_time():
    time = int(request.form["time"])

    with open(BEST_TIME_FILE, "r") as f:
        best_time = int(f.read())

    if time < best_time:
        with open(BEST_TIME_FILE, "w") as f:
            f.write(str(time))

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)


