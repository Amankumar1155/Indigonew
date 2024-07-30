import requests

# RapidAPI Key
RAPIDAPI_KEY = "40fe215ac1msh3b7bb3bd33e4754p1f573djsn43d2ffb8125b"


def get_flight_status(flight_id):
    # Replace with actual RapidAPI URL
    url = "https://flight-info.p.rapidapi.com/flight-status"
    querystring = {"flight_id": flight_id}
    headers = {
        # Replace with actual RapidAPI Host
        "X-RapidAPI-Host": "flight-info.p.rapidapi.com",
        "X-RapidAPI-Key": RAPIDAPI_KEY
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return None

