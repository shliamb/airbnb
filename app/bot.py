from keys import telegram
from get_exel import get_exel_file
from worker_db import get_count_rooms_not_None
import telebot
from telebot import types
import asyncio

# Токен, который вы получили от BotFather
TOKEN = telegram

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я эхо-бот. Напиши мне что-нибудь, и я отправлю это обратно!")


# Обработчик команды '/exel'
@bot.message_handler(commands=['exel'])
def total_id(message):
    file_exel = get_exel_file()
    with open(file_exel, "rb") as exel_file:
        bot.send_document(message.chat.id, exel_file)
    bot.reply_to(message, "Вот ваш Excel файл!")


# Обработчик команды '/count'
@bot.message_handler(commands=['count'])
def count_is_not(message):
    count = asyncio.run(get_count_rooms_not_None())
    bot.reply_to(message, f"Обработанных записей: {count}")


# Обработчик команды '/start'
@bot.message_handler(commands=['menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("4", callback_data='menu1')
    btn2 = types.InlineKeyboardButton("3", callback_data='menu2')
    btn3 = types.InlineKeyboardButton("2", callback_data='menu3')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, "Создать отчет по колличеству bedroom:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == 'menu1':
        answer = 'Вы выбрали пункт меню 1'
    elif call.data == 'menu2':
        answer = 'Вы выбрали пункт меню 2'
    elif call.data == 'menu3':
        answer = 'Вы выбрали пункт меню 3'

    bot.send_message(call.message.chat.id, answer)




# # Обработчик для эхо-ответов на любые текстовые сообщения
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

# Запуск бота
bot.polling()