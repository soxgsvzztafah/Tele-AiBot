import os
import telebot

bot = telebot.TeleBot("API Key Here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm Dark Devil Chat Bot. Created by Malindu Nimsara")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message.chat.id, "Hello, son of a bitch!")

bot.polling()
