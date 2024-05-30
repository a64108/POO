"""
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira
"""

from flask import Flask, request, jsonify, render_template
import sqlite3
import psutil
import time
import os

app = Flask(__name__)       #inicia flask e indica a db
DATABASE = 'sensors.db'

def get_db(): # getter que faz conexao com a db e busca info por coluna
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def insert_sensor_readings():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Verifica se ha items para ler na db
    cursor.execute("SELECT COUNT(*) FROM Reading")
    count = cursor.fetchone()[0]

    # Senao ha ele insere um leitura tipo placeholder
    if count == 0:
        sql = """
            INSERT INTO Reading (idSensor, value, timestamp)     
            VALUES (?, ?, ?)
        """

        sensor_id = 1  # Assumindo que o sensor_id 1 corresponde ao sensor de CPU
        reading_value = psutil.cpu_percent(interval=1)
        timestamp = int(time.time())
        data = (sensor_id, reading_value, timestamp)
        cursor.execute(sql, data)
        conn.commit()

    cursor.close()
    conn.close()

@app.route('/') #define homepage do site
def index():
    return render_template('index.html')

@app.route('/api/sensors', methods=['GET']) # vai buscar leituras dos sensores e retorna em formato JSON
def get_sensors():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT R.idReading, S.name as sensorName, R.timestamp, R.value
        FROM Reading R
        JOIN Sensor S ON R.idSensor = S.idSensor
    """)
    readings = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([dict(row) for row in readings])

if __name__ == '__main__':
    # Call the function to insert sensor readings
    insert_sensor_readings()
    
    # Run the Flask application
    app.run(debug=True)
