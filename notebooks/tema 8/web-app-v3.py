# web-app-v3.py
from flask import Flask, render_template

app = Flask(__name__)

things = [
    {
        "id": 1,
        "name": "Prometheus",
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("thing.html", title="Things (v3)", thing=things[0])


if __name__ == "__main__":
    app.run(debug=True)
