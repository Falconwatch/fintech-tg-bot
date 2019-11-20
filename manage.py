#!/usr/bin/env python
import os
import sys
import telebot
import requests
import json

bot = telebot.TeleBot('1029982015:AAGv7XUpiJrokPtUsSzxRmxDacoDbV59D5A')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20191117T205104Z.3ecf8e2efab662cd.262088c507c9012d2a5895fcfbc5624a17dd65ac'
    text = message.text
    lang = 'ru-en'

    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    result = json.loads(r.text)
    result1 = ' '.join(result['text'])
    bot.send_message(message.from_user.id, result1)






if __name__ == "__main__":
    bot.polling(none_stop=True, interval=1)