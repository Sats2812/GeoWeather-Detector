import requests
import json

#Location API 

send_url = "http://api.ipstack.com/check?access_key=7a0aea7209cd096becd25c65544abe30"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']

# ##For weather api

api_key= "d87983dad5a4a9fb5f73635bfd08bc3f"
base_url="http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city
req=requests.get(complete_url)
y=req.json()
x=y["main"]
temp=x["temp"]-273.15
temp=round(temp,2)
feel=x["feels_like"]-273.15
feel=round(feel,2)
min=x["temp_min"]-273.15
min=round(min,2)
max=x["temp_max"]-273.15
max=round(max,2)
weather_description = y["weather"][0]["description"]
