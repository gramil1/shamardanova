import requests, os
import telebot
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))

# Используем бесплатный API для получения курсов валют, например, exchangeratesapi.io

EXCHANGE_API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши 'курс' и я покажу текущие курсы валют.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == "курс":
        try:
            response = requests.get(EXCHANGE_API_URL)
            data = response.json()
            rates = data['rates']
            
           
            currency_message = (
                f"Курс валют относительно USD:\n"
                f"EUR: {rates['EUR']}\n"
                f"RUB: {rates['RUB']}\n"
                f"GBP: {rates['GBP']}\n"
                f"JPY: {rates['JPY']}\n"
                f"CNY: {rates['CNY']}\n"  
            )
        except Exception as e:
            currency_message = f"Не удалось получить данные о курсах валют. Ошибка: {e}"

        bot.reply_to(message, currency_message)
    else:
        bot.reply_to(message, "Напиши 'курс' для получения актуальных курсов валют.")

# Запускаем бота
bot.polling(none_stop = True, interval = 0)