from keys import telegram
from get_exel import get_exel_file
import telebot

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


# Обработчик для эхо-ответов на любые текстовые сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запуск бота
bot.polling()