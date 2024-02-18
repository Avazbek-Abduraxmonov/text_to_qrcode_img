import telebot
import requests
token = 'Your_Bot_Token'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '✋ Assalomu Aleykum botimizga xush kelibsiz\n🤖 Botni ishlatish uchun text kiriting')

@bot.message_handler(func=lambda message: True)
def sxema_message(message):
    text = message.text
    bot.send_photo(message.chat.id, requests.get(f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}").content)

bot.polling()
