import os
import telebot
from efundi import efundi
from keep_alive import keep_alive

keep_alive()

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)
@bot.message_handler(commands=['greet'])
def greet(message):
  bot.send_message(message.chat.id, 'Hello!')

@bot.message_handler(commands=['ticket'])
def ticket(message):
  bot.send_message(message.chat.id, 'Starting ticket process!')
  efundi()
  bot.send_message(message.chat.id, 'Done!')
bot.polling()