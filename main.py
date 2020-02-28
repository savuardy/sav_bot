import telebot
import schedule
import requests
import json

keys = json.load(open("keys.json"))
bot_api_key = keys["bot_api_key"]
appid = keys["appid_key"]

bot = telebot.TeleBot(bot_api_key)

@bot.message_handler(content_types = ['text','location'])
def get_text_messages(message):
    if message.text == "/start":
        print("Enter your city, please, or use geo")
    elif message.content_type == 'text':
        weather_writer_text(message.text)
    elif message.content_type == 'location':
        weather_writer_geo(message)
 
def weather_writer_geo(message):
    lat = message.location.latitude
    lon = message.location.longitude
    try:
        result = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,appid))
        weather_data = result.json()
        print(str(weather_data))
        print("conditions:", weather_data['weather'][0]['description'])
        print("temp:", int(weather_data['main']['temp']-273))
        print("temp_min:", int(weather_data['main']['temp_min']-273))
        print("temp_max:", int(weather_data['main']['temp_max']-273))
    except Exception as ex:
        print(ex)

def weather_writer_text(message):
    s_city = message
    try:
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(s_city,appid))
        data = res.json()
        print("conditions:", data['weather'][0]['description'])
        print("temp:", int(data['main']['temp']-273))
        print("temp_min:", int(data['main']['temp_min']-273))
        print("temp_max:", int(data['main']['temp_max']-273))
    except Exception as ex:
        print(ex)
#schedule.every().day.do(weather_writer)


bot.polling(none_stop=True, interval = 0)