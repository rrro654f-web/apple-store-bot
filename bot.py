from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text = """
🌟 <b>Вітаємо в нашому магазині!</b> 🍏

🛍️ <b>Для перегляду товарів натисніть кнопку "Магазин"</b>
"""
    
    keyboard = [
        [InlineKeyboardButton("🛍️ Магазин", url="t.me/AppleStoreUk_bot/Shop")],
        [InlineKeyboardButton("📱 Instagram", url="https://instagram.com/your_profile")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(start_text, reply_markup=reply_markup, parse_mode="HTML")

def main():
    application = Application.builder().token("7460415583:AAFLutgu1nva78UxleLGJcWc4BVJAH5RIzo").build()
    application.add_handler(CommandHandler("start", start_command))
    print("✅ Бот запущен! Ищи @AppleStoreUk_bot в Telegram")
    application.run_polling()

if __name__ == "__main__":
    main()
