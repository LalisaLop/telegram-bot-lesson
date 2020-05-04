import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from utils import button_handler

def start(update, context):
    get_name = update.message.text.split(' ')[1]
     
    keyboards = [
        [InlineKeyboardButton('Profil Bilgisi', callback_data=f'1 {get_name}')],
        [InlineKeyboardButton('Profil Timeline"ı', callback_data=f'2 {get_name}')],
    ]
    markup = InlineKeyboardMarkup(keyboards)
    update.message.reply_text('Lütfen birini seçiniz:', reply_markup=markup)

def buttons(update, context):
    query = update.callback_query
    query.answer()
    response = button_handler(query.data)
    query.edit_message_text(text=response, parse_mode=ParseMode.MARKDOWN_V2)

def runner():
    updater = Updater('token', use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('github', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(buttons))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    runner()
