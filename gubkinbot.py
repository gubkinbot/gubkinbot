import telebot
import yaml
from os import path as os_path

config_path = os_path.abspath(os_path.join(os_path.dirname(__file__), 'config.yml'))
config = yaml.safe_load(open(config_path))

bot = telebot.TeleBot(config['TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'Моя твоя не понимать...', parse_mode='HTML')
        
bot.infinity_polling()
