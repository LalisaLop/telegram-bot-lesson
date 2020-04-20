from telegram.ext import Updater, CommandHandler
import requests


def get_followed(id):
    link = f'https://www.instagram.com/{id}/?__a=1'
    user = requests.get(link)
    return user.json()['graphql']['user']


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=f'update_id={update.update_id}')


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def get_instagram_name(bot, update):
    get_name = update.message.text.split(' ')
    get_user = get_followed(get_name[1])
    get_count = get_user['edge_followed_by']['count']
    bot.send_message(
        chat_id=update.message.chat_id,
        text=f'{get_name[1]} isimli kullanicinin takipcisi sayisi {get_count}')


def post_instagram_profile_pic(bot, update):
    get_name = update.message.text.split(' ')
    get_user = get_followed(get_name[1])
    get_pic_url = get_user['profile_pic_url_hd']
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=get_pic_url)


def runner():
    updater = Updater('Token')
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('echo', echo))
    dp.add_handler(CommandHandler('instagram', get_instagram_name))
    dp.add_handler(CommandHandler('instagram_pic', post_instagram_profile_pic))
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    runner()
