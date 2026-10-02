import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from app import keep_alive

keep_alive()  # запускает Flask в отдельном потоке

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! Я твой первый бот. Я работаю на бесплатном хостинге. Отправь /help, чтобы узнать, что я умею."
    )

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Доступные команды:\n/start - Приветствие\n/help - Это сообщение"
    )

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("Не найден BOT_TOKEN! Установи его в переменных окружения.")

    application = ApplicationBuilder().token(token).connect_timeout(20).read_timeout(30).pool_timeout(10).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    print("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()
