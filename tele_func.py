import schedule
import requests
import json
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import ConversationHandler
import logging
import database
keys = json.load(open("keys.json"))
bot_api_key = keys["bot_api_key"]
appid = keys["appid_key"]
prev_answer = " "

updater = Updater(token = bot_api_key, use_context = True)
dispatcher = updater.dispatcher

def start(update, context): #start command handler  func gives the "hello"-message
    context.bot.send_message(chat_id = update.effective_chat.id, text = "I'm a bot, that will help you with everyday morning forecast. Use /add_city or /add_city_geo")
    database.new_user_reg(update.effective_chat.id)

def add_city(update, context):
    user_says = " ".join(context.args)
    city_mode(update,context, user_says)

#def add_city_geo(update, context):



def unknown(update, context):#unknow command handler is
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def weather_text_response(update, context, result):
    weather_data = result.json()
    current_condition_string = ("Current weather: '{}'".format(weather_data['weather'][0]['description']))
    current_temp_string = ("Current temperature: {}℃".format(int(weather_data['main']['temp']-273)))
    minimum_temp_string = ("Minimal temperature: {}℃".format(int(weather_data['main']['temp_min']-273)))
    maximum_temp_string = ("Maximal temperature: {}℃".format(int(weather_data['main']['temp_max']-273)))
    context.bot.send_message(chat_id = update.effective_chat.id, text = "This is your weather forecast:\n{}\n{}\n{}\n{}".format(
            current_condition_string,
            current_temp_string, 
            minimum_temp_string,
            maximum_temp_string))

def geo_mode(update, context): #geo handler func
    if prev_answer == "/add_city_geo":
        try: 
            lat = update.message.location.latitude
            lon = update.message.location.longitude
            result = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,appid))
            weather_text_response(update, context, result)
        except Exception as ex:
            print(ex)

def city_mode(update, context,text):
    try:
        city = text
        result = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,appid))
        weather_text_response(update, context, result)
        database.adding_city_text(city, update.effective_chat.id)
    except Exception as ex:
        print(ex)


    