import requests

def fetch():
    try:
        header = {"User-Agent": "UmarLearningProject/0.1 (ISS source comparison test)"}
        r = requests.get('https://api.wheretheiss.at/v1/satellites/25544', timeout=6, headers=header)

        data = r.json()
        timestamp = data["timestamp"]
        latitude = float(data["latitude"])
        longitude = float(data['longitude'])
        return timestamp, latitude, longitude

    except Exception as e:
        print("Exception occured. :(")
        print(e)


    