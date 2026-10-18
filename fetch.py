import requests

def fetch():
    try:
        r = requests.get('http://api.open-notify.org/iss-now.json', timeout=6)
        # check if GET worked
        print("Status of GET:", r.status_code)


        print("Content:")
        print(r.text)
        data = r.json()
        timestamp = data["timestamp"]
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]['longitude'])
        return timestamp, latitude, longitude

    except Exception as e:
        print("Exception occured. :(")
        print(e)


    