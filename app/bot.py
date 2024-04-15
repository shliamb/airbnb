from keys import telegram
from get_exel import get_exel_file
from worker_db import get_id_passed_false_count, get_all_airbnb_airdna_good_count, get_point
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



# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в парсер Airbnb. Парсер постоянно собирает и обновляет данные в базу данных. В меню, вы можете ознакомиться с возможностями бота. Всего хорошего.")




#### MENU ####
bot_commands = [
    BotCommand("exel", "Отчеты"),
    BotCommand("count", "Статистика"),
    #BotCommand("bd", ""),
    BotCommand("bd", "* Backup DB"), # 💾
]
bot.set_my_commands(bot_commands)


# #### EXEL ####
@bot.message_handler(commands=['exel'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_exel_1 = types.InlineKeyboardButton("📊 Все обработанные данные", callback_data='menu1')
    btn_exel_2 = types.InlineKeyboardButton("📈 По возрастанию кол. Bedroom", callback_data='menu2')
    btn_exel_3 = types.InlineKeyboardButton("📉 По убыванию кол. Bedroom", callback_data='menu3')
    markup.row(btn_exel_1)
    markup.row(btn_exel_2)
    markup.row(btn_exel_3)
    bot.send_message(message.chat.id, "📊 Выберите интересующий отчет:", reply_markup=markup)

#### count ####
@bot.message_handler(commands=['count'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_count_1 = types.InlineKeyboardButton("🔋 Объектов готовых к работе", callback_data='count1')
    btn_count_2 = types.InlineKeyboardButton("🪫 Объектов в очереди переобхода", callback_data='count2')
    btn_count_3 = types.InlineKeyboardButton("💵 Вилка $ обхода на данный момент", callback_data='count3')
    markup.row(btn_count_1)
    markup.row(btn_count_2)
    markup.row(btn_count_3)
    bot.send_message(message.chat.id, "🧮 Выберите интересующую статистику:", reply_markup=markup)

# menu1
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
            file_exel = asyncio.run(get_exel_file(choice))
            with open(file_exel, "rb") as exel_file:
                bot.send_document(call.message.chat.id, exel_file)

        elif call.data == 'menu2':
            choice = "2"
            file_exel = asyncio.run(get_exel_file(choice))
            with open(file_exel, "rb") as exel_file:
                bot.send_document(call.message.chat.id, exel_file)

        elif call.data == 'menu3':
            choice = "3"
            file_exel = asyncio.run(get_exel_file(choice))
            with open(file_exel, "rb") as exel_file:
                bot.send_document(call.message.chat.id, exel_file)

        elif call.data == 'count1':
            file_exel = asyncio.run(get_all_airbnb_airdna_good_count())
            bot.send_message(call.message.chat.id, f"Объектов готовых к работе: {file_exel} объект.")


        elif call.data == 'count2':
            file_exel = asyncio.run(get_id_passed_false_count())
            bot.send_message(call.message.chat.id, f"В ожидании обхода: {file_exel} объект.")

        elif call.data == 'count3':
            data = asyncio.run(get_point(1))
            if data is not None:
                price_min = data.price_min
                price_max = data.price_max
            bot.send_message(call.message.chat.id, f"На данный момент парсер проходит\n диапазон от {price_min}$ до {price_max}$")





            # Получение времени затраченого на формирование отчета
        current_end = get_time_utcnow()
        if current_start is not None and current_end is not None:
            difference = float(current_end) - float(current_start)
            bot.send_message(call.message.chat.id, f"Выполнение запроса заняло: {round(difference, 2)} мин.")
        else:
            bot.send_message(call.message.chat.id, f"Спасибо за ожидание.")
    finally:
        # По завершении обработки запроса устанавливаем флаг
        action_done.set()
#####












# # Запуск бота
# bot.polling()



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
        time.sleep(60)

if attempts == max_attempts:
    print("Превышено максимальное количество попыток. Завершение работы.")