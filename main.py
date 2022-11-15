import requests
import os
from twilio.rest import Client


OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "ACa28cefa0f6a1f368f47dc93e279c22c1"
auth_token = "4bd2624c06975cd4e66f6bd6e8693777"

twilio_number = "+16693221450"
target_number = "+919098295555"

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