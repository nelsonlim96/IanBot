from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

token = os.environ['TELEGRAM_TOKEN']

def start(bot, update):
    update.message.reply_text('Hi!')

def send_help(bot, update):
    update.message.reply_text("Help!")
    
def echo(bot, update):
    update.message.reply_text(update.message.text)
    
def main():
    NAME = "ian-bot"
    PORT = os.environ.get('PORT')

    updater = Updater(token)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',send_help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=token)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME,token))
    updater.idle()

if __name__ == '__main__':     
    main()