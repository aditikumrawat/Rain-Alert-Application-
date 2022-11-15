import requests
import os
from twilio.rest import Client


OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "XXXXXXXXXXXXXXXX"
account_sid = "XXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXX"

twilio_number = "XXXXXXX"
target_number = "+91XXXXXXXXXX"

weather_parameter = {
    "lat" : 22.718670 ,
    "lon" : 75.855713 ,
    "appid" : API_KEY ,
    "exclude" : "current,minutely,daily"
}


response = requests.get(OWN_ENDPOINT, params = weather_parameter)
response.raise_for_status()

weather_data = response.json()["hourly"][:12]

will_rain =  False

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True 

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                        .create(
                            body="\n It's going to rain today.",
                            from_='+16693221450',
                            to= target_number
                            )
    print(message.status)
    
    
    
# TO RUN IT ON SERVER WE HAVE TO CREATE A PROXY SERVER BECAUSE DON'T HAVE SPECIFIC IP

# firstly have to import the module as below:-
# from twilio.http.http_client import TwilioHttpClient

# Created a proxy server 
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https' : os.environ['https_proxy']}
# client = Client(account_sid, auth_token, http_client = proxy_client)
