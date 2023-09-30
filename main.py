import requests
import smtplib
from keys import API_KEY, MY_EMAIL, MY_PASSWORD

OPEN_WEATHER_MAP_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'

#-----------------WEATHER API-----------------------------

weather_params = {
    'lat':-19.865010,
    'lon':-43.983825,
    'appid': API_KEY,
}

response = requests.get(OPEN_WEATHER_MAP_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()


current_days_forecast = weather_data['list'][:5]
# print(current_days_forecast) #Debugging

current_days_ids = []

for hour in current_days_forecast:
    weather_id = hour['weather'][0]['id']
    current_days_ids.append(weather_id)
    # print(weather_id) #Debugging

# print(current_days_ids) #Debugging

rain_today = False
for id in current_days_ids:
    if id < 700:
        rain_today = True

message = "Subject:Rain Expected Today\n\nIt might rain today; you should consider carrying an umbrella."

#------------------GMAIL API-------------------------------------
def rain_warning():
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)
    except:
        print('Error sendind the email')
    else:
        print('email sent')


if rain_today == True:
    # print(message) #Debugging
    rain_warning()

