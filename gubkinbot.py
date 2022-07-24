import telebot
import yaml
from os import path as os_path
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

config_path = os_path.abspath(os_path.join(os_path.dirname(__file__), 'config.yml'))
config = yaml.safe_load(open(config_path))

bot = telebot.TeleBot(config['TOKEN'])

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton('Done', callback_data='DONE'))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: telebot.types.CallbackQuery):
	bot.answer_callback_query(call.id, call.data)
	bot.edit_message_reply_markup(chat_id=call.message.chat.id, reply_markup=gen_markup())

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'Не знаю, что и сказать...', parse_mode='HTML')
        
bot.infinity_polling()
