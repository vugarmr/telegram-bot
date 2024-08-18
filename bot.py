from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os

# Убедитесь, что ваш токен установлен в переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Создание и запуск бота
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Используйте команды /break5, /break7, /break10 для запроса перерыва.')

async def break_request(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("5 минут", callback_data='5')],
        [InlineKeyboardButton("7 минут", callback_data='7')],
        [InlineKeyboardButton("10 минут", callback_data='10')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите длительность перерыва:', reply_markup=reply_markup)

async def handle_break_request(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    choice = query.data
    await query.edit_message_text(text=f"Запрос на перерыв на {choice} минут принят!")

async def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("break", break_request))
    application.add_handler(CallbackQueryHandler(handle_break_request))

    # Запуск бота
    await application.run_polling()

# Вызов основной функции в асинхронном контексте
if __name__ == '__main__':
    import asyncio
    # Используйте asyncio.run только если вы уверены, что цикл событий не запущен
    asyncio.get_event_loop().run_until_complete(main())
