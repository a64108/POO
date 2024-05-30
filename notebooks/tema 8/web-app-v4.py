# web-app-v4.py
from flask import Flask, render_template

app = Flask(__name__)

things = [
    {
        "id": 1,
        "name": "Prometheus",
        "local": "@lab. 163 / ISE /UAlg",
        "sensors": [
            {"sensor_name": "mem_sensor", "units": "percent"},
            {"sensor_name": "cpu_sensor", "units": "percent"},
        ],
    },
    {
        "id": 2,
        "name": "Zeus",
        "local": "@lab. 163 / ISE /UAlg",
        "sensors": [
            {"sensor_name": "temperature", "units": "numerical"},
            {"sensor_name": "humidity", "units": "percent"},
        ],
    },
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("things-lista.html", title="Things (v4)", things=things)


if __name__ == "__main__":
    app.run(debug=True)
