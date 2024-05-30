# web-app-v2.py
from flask import Flask

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
    html = f"""
        <html>
            <head>
                <title>Things (v2)</title>
            </head>
            <body>
                <h1>Thing: {things[0]['name']}!</h1>
            </body>
        </html>
        """

    return html


if __name__ == "__main__":
    app.run(debug=True)
