from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

# Токен вашего бота (получите у @BotFather)
TOKEN = "8142014877:AAE2U2_gv4jtC7y4lpsknNo0SHdsEuJW80U"

# Обработчик команды /start
async def start(update: Update, context):
    # Создаем Reply-клавиатуру (кнопки внизу экрана)
    keyboard = [
        [KeyboardButton("Сайт"), KeyboardButton("Помощь")],
        [KeyboardButton("Отправить контакт", request_contact=True)],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    # Отправляем сообщение с кнопками
    await update.message.reply_text(
        "Привет! Выберите действие:",
        reply_markup=reply_markup
    )

# Обработчик нажатий на Inline-кнопки
async def button_click(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Вы нажали: {query.data}")

# Обработчик обычных сообщений
async def handle_message(update: Update, context):
    text = update.message.text
    if text == "Сайт":
        # Создаем Inline-кнопки (внутри сообщения)
        inline_keyboard = [
            [InlineKeyboardButton("Сайт", url="https://apagroup.pro")]
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)
        
        await update.message.reply_text(
            "Хотите перейти на наш сайт?",
            reply_markup=reply_markup
        )
    elif text == "Помощь":
        await update.message.reply_text("Запрос отправлен, ожидайте оператора.")

# Основная функция
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    app.run_polling()

if __name__ == "__main__":
    main()
