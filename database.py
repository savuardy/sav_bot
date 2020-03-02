from tinydb import TinyDB, Query

db = TinyDB('/home/savuard/git_projects/sav_bot/database.json')
user = Query()
city_list = []

def new_user_reg(chat_id):
    already_started = False
    for item in db:
        if item['chat_id'] == chat_id:
            already_started = True

    if already_started is False:
        db.insert({ chat_id : { 'chat_id': chat_id, 'cities_list' : []}})

def adding_city_text(city, chat_id):
    global city_list
    city_list.append(city)
    db.upsert({'cities_list' : city_list}, user['chat_id'] == chat_id)
