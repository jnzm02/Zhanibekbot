import telebot
import schedule
import time
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('722fc9a6f1d1610d49dc213c063dc94c')
bot = telebot.TeleBot('2089345480:AAFva_L1bfoktLMlfKvJOXVQ6jX2zlwkoF4')
mgr = owm.weather_manager()

#weather
@bot.message_handler(content_types=['text'])
def send_weather_status(message):
	observation = mgr.weather_at_place(message)
	w = observation.weather
	wt = w.temperature('celsius')["temp"]
	bot.send_message(message.chat.id, str(wt) + str(176) + "C")

bot.polling ()
