import sqlite3

db_name = "iss_positions.db"

def create_table():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS iss_positions (
    timestamp INTEGER PRIMARY KEY,
    latitude REAL NOT NULL CHECK (latitude >= -90 AND latitude <= 90),
    longitude REAL NOT NULL CHECK (longitude >= -180 AND longitude <= 180)
    )
    """)

    connection.commit()

    connection.close()

def insert_position(timestamp, latitude, longitude):
    connection = sqlite3.connect(db_name)

    cursor = connection.cursor()

    try:
        cursor.execute("INSERT OR IGNORE INTO iss_positions (timestamp, latitude, longitude) VALUES (?, ?, ?)", (timestamp, latitude, longitude))
    except:
        print("Error inserting :(")
        connection.close()

    connection.commit()
    connection.close()