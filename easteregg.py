def is_over_malaysia(lat, lon):
    peninsular = 1.2 <= lat <= 6.7 and 99.6 <= lon <= 104.5
    borneo = 0.9 <= lat <= 7.4 and 109.6 <= lon <= 119.3

    if peninsular or borneo:
        print("ISS is above Malaysia. Wave and smile!")
        return True
    return False