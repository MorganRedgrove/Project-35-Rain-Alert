import requests
from twilio.rest import Client

api_key = ""
parameters = {
    "lat": 45.5017,
    "lon": -73.5673,
    "appid": api_key,
    "exclude": "current,minutely,daily,"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
data = response.json()

weather_list = [data["hourly"][num]["weather"][0]["id"] for num in range(0,12)]

for code in weather_list:
    if code <700:
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                             body="It will rain today.",
                             from_='+12182967152',
                             to='+447496596790'
                         )

        print(message.status)
