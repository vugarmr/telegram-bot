# -*- coding: utf-8 -*-

import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Бот работает!')

def main() -> None:
    # Создайте экземпляр Updater и передайте ему ваш токен бота.
    updater = Updater(os.getenv("TELEGRAM_BOT_TOKEN"))
    dispatcher = updater.dispatcher

    # Обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
