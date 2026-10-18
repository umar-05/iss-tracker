import requests






try:
    r = requests.get('http://api.open-notify.org/iss-now.json', timeout=6)
    # check if GET worked
    print("Status of GET:", r.status_code)


    print("Content:")
    print(r.text)
except:
    print("Exception occured. :(")