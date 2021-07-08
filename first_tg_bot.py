import telebot as tb
import config
import random

from telebot import types

bot = tb.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['huj'])
def sam_takoy(message):
    sti = open('hey.webp', 'rb')
    mainKeyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    but1 = types.KeyboardButton('Люблю')
    but2 = types.KeyboardButton('кошек')
    mainKeyboard.add(but1, but2)
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'пизда', reply_markup = mainKeyboard)
    
@bot.message_handler(content_types = ['text'])
def recalll(message):
    
    if message.chat.type == 'private':
        if message.text == 'Люблю':
            bot.send_message(message.chat.id, 'А я тебя люблю')
        else:
            bot.send_message(message.chat.id, 'нажми Люблю')
# RUN
bot.polling(none_stop = True)