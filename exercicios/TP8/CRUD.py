"""
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira

Codigo dado por notebook
"""

import sqlite3
import psutil


conn = sqlite3.connect("sensors.db")
cursor = conn.cursor()

# Prepare the sql statement for the new location
sql = """
    INSERT INTO location (name, description) 
    VALUES (?, ?)
"""

data = ("Prometheus Server", "Prometheus Server @ lab. 163 / ISE /UAlg")

# Execute the sql statement and get the new location id
cursor.execute(sql, data)
conn.commit()

location_id = cursor.lastrowid
location_id

sql = "delete from location where idLocation in (2,3)"
cursor.execute(sql)
conn.commit()

sql = """
    INSERT INTO Unit (unit, description) 
    VALUES (?, ?)
"""

data = ("percent", "percentage of usage")

try:
    cursor.execute(sql, data)  # statement + tuple with the data
    conn.commit()
except sqlite3.IntegrityError:
    print("Unit with value 'percent' already exists.")

sql = """
    INSERT INTO Sensor (idLocation, name, unit)
    VALUES (:idLocation, :name, :unit)
"""

data = {
    "idLocation": location_id,
    "name": "cpu_sensor_01",
    "unit": "percent",
}

cursor.execute(sql, data)
sensor_id = cursor.lastrowid
conn.commit()
sensor_id


sql = """
    INSERT INTO Reading (idSensor, value)     
    VALUES (:idSensor, :value)
"""

for _ in range(20):
    data = {
        "idSensor": sensor_id,
        "value": psutil.cpu_percent(interval=1),
    }
    cursor.execute(sql, data)
    conn.commit()
    print(".", end="")


cursor.close()
conn.close()


conn = sqlite3.connect("sensors.db")
cursor = conn.cursor()

sql = """
    SELECT idLocation, name, description 
    FROM location 
    WHERE description LIKE "%163%"
"""

cursor.execute(sql)

for (idLocation, name, description) in cursor:
    print(f"id: {idLocation}\n\t name: {name} \n\t description: {description}")


sql = """
    SELECT idReading, idSensor, timestamp, value 
    FROM reading 
    WHERE value BETWEEN ? and ?
"""
data = (5, 30)

cursor.execute(sql, data)

for (idReading, idSensor, timestamp, value) in cursor:
    print(f"idReading: {idReading}\n\t idSensor: {idSensor} \n\t time: {timestamp} \n\t value: {value}")


sql = """
    SELECT *
    FROM Location as L
    INNER JOIN Sensor AS S ON L.idLocation = S.idLocation
    INNER JOIN Unit AS U ON S.unit = U.unit
    INNER JOIN Reading AS R ON S.idSensor = R.idSensor
    WHERE VALUE BETWEEN :low AND :high
    ORDER BY VALUE
"""

data = {
    "low": 1,
    "high": 2,
}

cursor.execute(sql, data)

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
