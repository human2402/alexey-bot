from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging

from bs4 import BeautifulSoup
import requests
from random import randrange

def getCongrats():
    randomPage = randrange(1,10)
    htmlText = requests.get('https://pozdravok.ru/pozdravleniya/lyubov/spokoynoy-nochi/'+str(randomPage)).text
    soup = BeautifulSoup(htmlText, 'lxml')
    grettings = soup.find('p', class_ = "sfst").text.replace('<br/>', " ")
    return str(grettings + "\nluv u 💕")

updater = Updater(token="1411741351:AAHVLq_m_S8a1OT_iNg5ber7cRLrjF9Chx4", use_context= True)

dispatecher = updater.dispatcher

logging.basicConfig(format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", level= logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id = -413441762, text= "effective chat update.effective_chat.id"+ str(update.effective_chat.id))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Just like that - "+ update.message.text)

def good_night(update, context):
    context.bot.send_message(chat_id=-413441762, text=getCongrats())

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
good_night_handler = CommandHandler('night', good_night)

dispatecher.add_handler (start_handler)
dispatecher.add_handler(echo_handler)
dispatecher.add_handler(good_night_handler)

updater.start_polling()




