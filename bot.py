from telegram import Update, ParseMode, ReplyKeyboardRemove
from telegram.ext import CommandHandler, CallbackContext, Updater, Defaults, PicklePersistence

from models.user import User

import os
import localization as lp

# BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_TOKEN = '434941139:AAG1Apadczm8qIT9AzT-E3BLRI9_wRIZtd4'

def command_start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    username = update.effective_user.username

    #user = User.where('user_id', '=', user_id).first()
    update.message.reply_text(
        lp.START_MESSAGE,
        reply_markup=ReplyKeyboardRemove()
    )
    
def main():
    defaults = Defaults(parse_mode=ParseMode.MARKDOWN, timeout=120)
    persistence = PicklePersistence('persistence_storage')

    updater = Updater(BOT_TOKEN, persistence=persistence, defaults=defaults)
    add_handler = updater.dispatcher.add_handler

    add_handler(CommandHandler('start', command_start))

    updater.start_polling()
    updater.idle()

if __name__ == main():
    main()
