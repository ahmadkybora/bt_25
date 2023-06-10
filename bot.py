from telegram import Update, ParseMode, ReplyKeyboardRemove
from telegram.ext import CommandHandler, CallbackContext, Updater, Defaults, PicklePersistence

from models.user import User

import os
import localization as lp

BOT_TOKEN = os.getEnv('BOT_TOKEN')

def command_start(update: Update, context: CallbackContext):
    user_id = update.effective.user_id
    user_name = update.effective.user_name

    user = User.where('user_id', '=', user_id).first()

    update.message.reply_text(lp.START_MESSAGE, reply_markup=ReplyKeyboardRemove())
    
def main():
    defaults = Defaults(parse_mode=ParseMode.MARKDOWN, timeout=120)
    persistance = PicklePersistence('persistence_storage')

    updater = Updater(BOT_TOKEN, persistance=persistance, defaults=defaults)
    add_handler = updater.dispatcher.add_handler

    add_handler(CommandHandler('start', command_start))