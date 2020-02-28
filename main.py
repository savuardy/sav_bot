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
    chat_id = message.chat.id
    if message.text == "/start":
        bot.send_message(text = "Enter your city, please, or use geo", chat_id = chat_id)
    if message.content_type == 'text':
            weather_writer_text(message.text, chat_id)
    if message.content_type == 'location':
            weather_writer_geo(message,chat_id)
 
def weather_writer_geo(message, chat_id):
    lat = message.location.latitude
    lon = message.location.longitude
    chat_id = message.chat.id
    try:
        result = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,appid))
        weather_data = result.json()
        current_condition_string = ("Current weather: '{}'".format(weather_data['weather'][0]['description']))
        current_temp_string = ("Current temperature: {}℃".format(int(weather_data['main']['temp']-273)))
        minimum_temp_string = ("Minimal temperature: {}℃".format(int(weather_data['main']['temp_min']-273)))
        maximum_temp_string = ("Maximal temperature: {}℃".format(int(weather_data['main']['temp_max']-273)))
        bot.send_message(chat_id = chat_id, text = "This is your weather forecast:\n{}\n{}\n{}\n{}".format(
            current_condition_string,
            current_temp_string, 
            minimum_temp_string,
            maximum_temp_string))
    except Exception as ex:
        print(ex)

def weather_writer_text(message, chat_id):
    s_city = message
    try:
        result = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(s_city,appid))
        weather_data = result.json()
        current_condition_string = ("Current weather:{}".format(weather_data['weather'][0]['description']))
        current_temp_string = ("Current temperature: {}℃".format(int(weather_data['main']['temp']-273)))
        minimum_temp_string = ("Minimal temperature: {}℃".format(int(weather_data['main']['temp_min']-273)))
        maximum_temp_string = ("Maximal temperature: {}℃".format(int(weather_data['main']['temp_max']-273)))
        bot.send_message(chat_id = chat_id, text = "This is your weather forecast:\n{}\n{}\n{}\n{}".format(
            current_condition_string,
            current_temp_string, 
            minimum_temp_string,
            maximum_temp_string))
    except Exception as ex:
        print(ex)
#schedule.every().day.do(weather_writer)


bot.polling(none_stop=True, interval = 0)