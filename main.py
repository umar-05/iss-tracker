from fetch import fetch
from store import create_table, insert_position
from easteregg import is_over_malaysia
import time


create_table()

try:
    while True:
        result = fetch()

        if result is None:
            print("Failed. Skipping :o")
        else:
            timestamp, latitude, longitude = result
            insert_position(timestamp, latitude, longitude)
            print(f"ISS Position at {timestamp}, Latitude: {latitude} Longitude: {longitude}")
            is_over_malaysia(latitude, longitude)
            
        time.sleep(5)

except KeyboardInterrupt:
    print("All stopped.")
