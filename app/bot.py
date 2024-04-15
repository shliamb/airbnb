from keys import telegram
from get_exel import get_exel_file
from worker_db import get_count_rooms_not_None
from datetime import datetime, timezone, timedelta
import telebot
from telebot import types
from telebot.types import BotCommand
import threading
import asyncio
import time


# Токен, который вы получили от BotFather
TOKEN = telegram

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)


# GET DAY AND TIME
def get_time_utcnow() -> time:
    current_time = datetime.now(timezone.utc).strftime("%M")
    return current_time






# Меню слева снизу
bot_commands = [
    BotCommand("menu", "Сформировать отчет"),
    BotCommand("count", "Обработанных записей"),
    BotCommand("bd", "BD"),
]
bot.set_my_commands(bot_commands)


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "")



# Обработчик команды '/count'
@bot.message_handler(commands=['count'])
def count_is_not(message):
    bot.send_chat_action(message.chat.id, 'typing') 
    count = asyncio.run(get_count_rooms_not_None())
    bot.reply_to(message, f"Обработанных записей: {count}")


# Обработчик команды '/menu'
@bot.message_handler(commands=['menu'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Без фильтра", callback_data='menu1')
    btn2 = types.InlineKeyboardButton("Bedroom по возрастанию", callback_data='menu2')
    btn3 = types.InlineKeyboardButton("Bedroom по убыванию", callback_data='menu3')
    markup.row(btn1)
    # markup.row(btn2)
    # markup.row(btn3)
    bot.send_message(message.chat.id, "Отчет по фильтрам:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)

    current_start = get_time_utcnow()

    # Функция для отправки действия "typing"
    def send_typing_action(chat_id):
        while not action_done.is_set():  # Пока флаг не установлен, отправляем "typing"
            bot.send_chat_action(chat_id, 'typing')
            time.sleep(3)  # Интервал в секундах между отправками действия "typing"

    # Флаг для отслеживания статуса обработки запроса
    action_done = threading.Event()

    # Запуск потока, который будет отправлять действие "typing"
    threading.Thread(target=send_typing_action, args=(call.message.chat.id,)).start()

    try:
        if call.data == 'menu1':
            choice = "1"
            file_exel = get_exel_file(choice)
            with open(file_exel, "rb") as exel_file:
                bot.send_document(call.message.chat.id, exel_file)

        # elif call.data == 'menu2':
        #     choice = "2"
        #     file_exel = get_exel_file(choice)
        #     with open(file_exel, "rb") as exel_file:
        #         bot.send_document(call.message.chat.id, exel_file)

        # elif call.data == 'menu3':
        #     choice = "3"
        #     file_exel = get_exel_file(choice)
        #     with open(file_exel, "rb") as exel_file:
        #         bot.send_document(call.message.chat.id, exel_file)

        current_end = get_time_utcnow()
        if current_start is not None and current_end is not None:
            difference = float(current_end) - float(current_start)
            bot.send_message(call.message.chat.id, f"Отчет готов.\nФормирование таблицы заняло {round(difference, 2)} мин.")
        else:
            bot.send_message(call.message.chat.id, f"Отчет готов.\nТаблица сформирована, спасибо за ожидание.")
    finally:
        # По завершении обработки запроса устанавливаем флаг
        action_done.set()






# # Запуск бота
#bot.polling()



max_attempts = 5
attempts = 0

while attempts < max_attempts:
    try:
        print("info: start bot")
        bot.polling()
        break
    except Exception as e:
        attempts += 1
        print(f"Произошла ошибка: {e}. Попытка {attempts} из {max_attempts}. Повторная попытка через 5 секунд...")
        time.sleep(5)

if attempts == max_attempts:
    print("Превышено максимальное количество попыток. Завершение работы.")