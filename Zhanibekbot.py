import telebot
# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps
# from colorama import init
# from colorama import Fore, Back, Style
# from aiogram import Bot, Dispatcher, executor, types

# owm = OWM('722fc9a6f1d1610d49dc213c063dc94c')
bot = telebot.TeleBot('1907049725:AAFnP14BCQ0XOHJWwGdV7LyxoAn4bCVP9jk')
# mgr = owm.weather_manager()

# init()
# print (Fore.BLACK)
# print (Back.CYAN)

# start & help commands
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Nizami, how are you doing?")

#echo bot
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


#weather
# @bot.message_handler(content_types=['text'])
# def send_echo(message):
# 	observation = mgr.weather_at_place(message.text)
# 	w = observation.weather
# 	wt = w.temperature('celsius')["temp"]
# 	answer = "The temperature in " + message.text + " is " + str(wt) +'\n\n'
# 	if (wt < 10):
# 		answer += "Now it is frozen in " + message.text +", you must to wear warm clothes!"
# 	elif (wt < 20):
# 		answer += "Now it is cold in " + message.text +", please wear warm clothes"
# 	else :
# 		answer += "Now it is warm in " + message.text +", you can wear whatever you want"
# 	bot.send_message(message.chat.id, answer)

bot.polling ( none_stop = True )	

# print (Back.YELLOW)
# print ("current temperature in this region " + str(st))

# if st > 25:
# 	print (Back.GREEN)
# 	x = " You can walk in the Shirt outside "
# elif st < 0:
# 	print (Back.MAGENTA)
# 	x = " It is too cold outside!!! \n YOU MUST WEAR WARM JACKET!!! "
# else:
# 	print (Back.RED)
# 	x = " You should wear warm clothes!!! "
# print (str(x))

# bot.polling()
