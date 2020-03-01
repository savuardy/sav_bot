import telebot
import schedule
import requests
import json
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import ConversationHandler
import logging
import tele_func 

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO) #This is a good time to set up the logging module, so you will know when (and why) things don't work as expected

updater =  tele_func.updater  #First, you have to create an Updater object.
dispatcher = tele_func.dispatcher   #For quicker access to the Dispatcher used by your Updater, you can introduce it locally
start_handler = CommandHandler('start', tele_func.start)
dispatcher.add_handler(start_handler) #adding start command handler
add_city_handler = CommandHandler('add_city', tele_func.add_city)
dispatcher.add_handler(add_city_handler)
# add_city_geo_handler = CommandHandler('add_city_geo', tele_func.add_city_geo)
# dispatcher.add_handler(add_city_geo_handler)
geo_handler = MessageHandler(Filters.location, tele_func.geo_mode)
dispatcher.add_handler(geo_handler)
unknown_handler = MessageHandler(Filters.command, tele_func.unknown)
dispatcher.add_handler(unknown_handler) # adding unknown command handler

updater.start_polling()
updater.idle()

#updater.start_polling()
# def echo(update, context): 
#     context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

# echo_handler = MessageHandler(Filters.text, echo)
# dispatcher.add_handler(echo_handler)




# bot = telebot.TeleBot(bot_api_key)

# @bot.message_handler(content_types = ['text','location'])
# def get_text_messages(message):             #replace with useable code
#     chat_id = message.chat.id
#     if message.text == "/start":
#         bot.send_message(text = "Enter your city, please, or use geo", chat_id = chat_id)
#     if message.content_type == 'text':
#             weather_writer_text(message.text, chat_id)
#     if message.content_type == 'location':
#             weather_writer_geo(message,chat_id)
 
# def weather_writer_geo(message, chat_id):
#     lat = message.location.latitude
#     lon = message.location.longitude
#     chat_id = message.chat.id
#     try:
#         result = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,lon,appid))
#         weather_data = result.json()
#         current_condition_string = ("Current weather: '{}'".format(weather_data['weather'][0]['description']))
#         current_temp_string = ("Current temperature: {}℃".format(int(weather_data['main']['temp']-273)))
#         minimum_temp_string = ("Minimal temperature: {}℃".format(int(weather_data['main']['temp_min']-273)))
#         maximum_temp_string = ("Maximal temperature: {}℃".format(int(weather_data['main']['temp_max']-273)))
#         bot.send_message(chat_id = chat_id, text = "This is your weather forecast:\n{}\n{}\n{}\n{}".format(
#             current_condition_string,
#             current_temp_string, 
#             minimum_temp_string,
#             maximum_temp_string))
#     except Exception as ex:
#         print(ex)

# def weather_writer_text(message, chat_id):
#     s_city = message
#     try:
#         result = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(s_city,appid))
#         weather_data = result.json()
#         current_condition_string = ("Current weather:{}".format(weather_data['weather'][0]['description']))
#         current_temp_string = ("Current temperature: {}℃".format(int(weather_data['main']['temp']-273)))
#         minimum_temp_string = ("Minimal temperature: {}℃".format(int(weather_data['main']['temp_min']-273)))
#         maximum_temp_string = ("Maximal temperature: {}℃".format(int(weather_data['main']['temp_max']-273)))
#         bot.send_message(chat_id = chat_id, text = "This is your weather forecast:\n{}\n{}\n{}\n{}".format(
#             current_condition_string,
#             current_temp_string, 
#             minimum_temp_string,
#             maximum_temp_string))
#     except Exception as ex:
#         print(ex)
# #schedule.every().day.do(weather_writer)


# bot.polling(none_stop=True, interval = 0)