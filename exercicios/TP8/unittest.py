"""
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira
"""

import unittest
import sqlite3
import os
import psutil

class TestCRUDOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a test database
        cls.db_name = "test_sensors.db"
        cls.conn = sqlite3.connect(cls.db_name)
        cls.cursor = cls.conn.cursor()
        
        cls.create_tables()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()
        os.remove(cls.db_name)

    @classmethod
    def create_tables(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS Location (
            idLocation INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Unit (
            unit TEXT PRIMARY KEY,
            description TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Sensor (
            idSensor INTEGER PRIMARY KEY AUTOINCREMENT,
            idLocation INTEGER NOT NULL,
            name TEXT NOT NULL,
            unit TEXT NOT NULL,
            FOREIGN KEY(idLocation) REFERENCES Location(idLocation) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY(unit) REFERENCES Unit(unit) ON UPDATE CASCADE ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS Reading (
            idReading INTEGER PRIMARY KEY AUTOINCREMENT,
            idSensor INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            value REAL NOT NULL,
            FOREIGN KEY(idSensor) REFERENCES Sensor(idSensor) ON UPDATE CASCADE ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS Alert (
            idAlert INTEGER PRIMARY KEY AUTOINCREMENT,
            idSensor INTEGER,
            description TEXT NOT NULL,
            cleared INTEGER,
            FOREIGN KEY(idSensor) REFERENCES Sensor(idSensor) ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
        cls.cursor.executescript(sql)

    def setUp(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_insert_location(self):
        sql = "INSERT INTO Location (name, description) VALUES (?, ?)"
        data = ("Test Location", "Test Description")
        self.cursor.execute(sql, data)
        self.conn.commit()

        location_id = self.cursor.lastrowid
        self.cursor.execute("SELECT * FROM Location WHERE idLocation=?", (location_id,))
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Test Location")
        self.assertEqual(result[2], "Test Description")

    def test_insert_unit(self):
        sql = "INSERT INTO Unit (unit, description) VALUES (?, ?)"
        data = ("percent", "percentage of usage")
        self.cursor.execute(sql, data)
        self.conn.commit()

        self.cursor.execute("SELECT * FROM Unit WHERE unit=?", ("percent",))
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], "percent")
        self.assertEqual(result[1], "percentage of usage")

    def test_insert_sensor(self):
        sql = "INSERT INTO Location (name, description) VALUES (?, ?)"
        location_data = ("Test Location", "Test Description")
        self.cursor.execute(sql, location_data)
        location_id = self.cursor.lastrowid
        self.conn.commit()

        sql = "INSERT INTO Sensor (idLocation, name, unit) VALUES (?, ?, ?)"
        sensor_data = (location_id, "cpu_sensor_01", "percent")
        self.cursor.execute(sql, sensor_data)
        self.conn.commit()

        sensor_id = self.cursor.lastrowid
        self.cursor.execute("SELECT * FROM Sensor WHERE idSensor=?", (sensor_id,))
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[1], location_id)
        self.assertEqual(result[2], "cpu_sensor_01")
        self.assertEqual(result[3], "percent")

    def test_insert_reading(self):
        sql = "INSERT INTO Location (name, description) VALUES (?, ?)"
        location_data = ("Test Location", "Test Description")
        self.cursor.execute(sql, location_data)
        location_id = self.cursor.lastrowid
        self.conn.commit()

        sql = "INSERT INTO Sensor (idLocation, name, unit) VALUES (?, ?, ?)"
        sensor_data = (location_id, "cpu_sensor_01", "percent")
        self.cursor.execute(sql, sensor_data)
        sensor_id = self.cursor.lastrowid
        self.conn.commit()

        sql = "INSERT INTO Reading (idSensor, value) VALUES (?, ?)"
        reading_data = (sensor_id, 10.0)
        self.cursor.execute(sql, reading_data)
        self.conn.commit()

        self.cursor.execute("SELECT * FROM Reading WHERE idSensor=?", (sensor_id,))
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[1], sensor_id)
        self.assertEqual(result[3], 10.0)

    def test_query_location(self):
        sql = "INSERT INTO Location (name, description) VALUES (?, ?)"
        location_data = ("Test Location", "Test Description")
        self.cursor.execute(sql, location_data)
        self.conn.commit()

        self.cursor.execute("SELECT idLocation, name, description FROM Location WHERE description LIKE ?", ("%Test%",))
        result = self.cursor.fetchall()

        self.assertTrue(len(result) > 0)
        self.assertEqual(result[0][1], "Test Location")
        self.assertEqual(result[0][2], "Test Description")

    def test_query_reading(self):
        sql = "INSERT INTO Location (name, description) VALUES (?, ?)"
        location_data = ("Test Location", "Test Description")
        self.cursor.execute(sql, location_data)
        location_id = self.cursor.lastrowid
        self.conn.commit()

        sql = "INSERT INTO Sensor (idLocation, name, unit) VALUES (?, ?, ?)"
        sensor_data = (location_id, "cpu_sensor_01", "percent")
        self.cursor.execute(sql, sensor_data)
        sensor_id = self.cursor.lastrowid
        self.conn.commit()

        sql = "INSERT INTO Reading (idSensor, value) VALUES (?, ?)"
        reading_data = (sensor_id, 10.0)
        self.cursor.execute(sql, reading_data)
        self.conn.commit()

        self.cursor.execute("SELECT idReading, idSensor, timestamp, value FROM Reading WHERE value BETWEEN ? AND ?", (5, 15))
        result = self.cursor.fetchall()

        self.assertTrue(len(result) > 0)
        self.assertEqual(result[0][1], sensor_id)

    def test_query_joined_data(self):
        sql = "INSERT INTO Location (name, description) VALUES (?, ?)"
        location_data = ("Test Location", "Test Description")
        self.cursor.execute(sql, location_data)
        location_id = self.cursor.lastrowid
        self.conn.commit()

        sql = "INSERT INTO Unit (unit, description) VALUES (?, ?)"
        unit_data = ("percent", "percentage of usage")
        self.cursor.execute(sql, unit_data)
        self.conn.commit()

        sql = "INSERT INTO Sensor (idLocation, name, unit) VALUES (?, ?, ?)"
        sensor_data = (location_id, "cpu_sensor_01", "percent")
        self.cursor.execute(sql, sensor_data)
        sensor_id = self.cursor.lastrowid
        self.conn.commit()

        sql = "INSERT INTO Reading (idSensor, value) VALUES (?, ?)"
        reading_data = (sensor_id, 1.5)
        self.cursor.execute(sql, reading_data)
        self.conn.commit()

        sql = """
        SELECT * FROM Location AS L
        INNER JOIN Sensor AS S ON L.idLocation = S.idLocation
        INNER JOIN Unit AS U ON S.unit = U.unit
        INNER JOIN Reading AS R ON S.idSensor = R.idSensor
        WHERE R.value BETWEEN ? AND ?
        ORDER BY R.value
        """
        self.cursor.execute(sql, (1, 2))
        result = self.cursor.fetchall()

        self.assertTrue(len(result) > 0)
        self.assertEqual(result[0][3], "Test Location")
        self.assertEqual(result[0][7], 1.5)

if __name__ == '__main__':
    unittest.main()
