import telebot
import yaml
from os import path as os_path

config_path = os_path.abspath(os_path.join(os_path.dirname(__file__), 'config.yml'))
config = yaml.safe_load(open(config_path))

bot = telebot.TeleBot(config['TOKEN'])

ids = [2528316, -1001770890678, 263965948, 95700052, 543148778, 1221981431, 245304345, 57180126, 713287828]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.find('-') > 0:
        bot.reply_to(message, 'Моя твоя не понимать...', parse_mode='HTML')
        

bot.infinity_polling()