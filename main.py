from fetch import fetch
from store import create_table, insert_position

# import needed table functionalities from store.py

create_table()
result = fetch()

if result is None:
    print("Failed. Skipping :o")
else:
    timestamp, latitude, longitude = result
    insert_position(timestamp, latitude, longitude)
