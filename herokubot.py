import logging
import os
import requests
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    update.effective_message.reply_text("Hi!")

def echo(bot, update):
    update.effective_message.reply_text(yandex(update.effective_message.text))

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

def yandex(message):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20191117T205104Z.3ecf8e2efab662cd.262088c507c9012d2a5895fcfbc5624a17dd65ac'
    text = message.text
    lang = 'ru-en'

    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    result = json.loads(r.text)
    return ' '.join(result['text'])

if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1029982015:AAGv7XUpiJrokPtUsSzxRmxDacoDbV59D5A"
    NAME = "tfs-tele-bot"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
