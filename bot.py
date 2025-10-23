from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import asyncio
import time

# Твій токен
BOT_TOKEN = "7460415583:AAFLutgu1nva78UxleLGJcWc4BVJAH5RIzo"

# Текст для /start
START_TEXT = """
🍏 <b>Ласкаво просимо до нашого магазину!</b> 🍏

Де ви знайдете тільки найкращу техніку Apple — нову та б/у за вигідними цінами! 😊

<b>Відчуйте якість Apple</b> з нашим асортиментом нових та сертифікованих пристроїв! 🍏

<b>Шукаєте надійну техніку Apple?</b> У нас є нові моделі та перевірені пристрої, що задовольнять навіть найвибагливіших покупців! 📱

<b>Обирайте нові та сертифіковані продукти Apple</b> — якість і інновації за доступною ціною тільки в нашому магазині! 💻
"""

# Текст для головного меню
MAIN_MENU_TEXT = """
🌟 <b>Вітаємо вас у нашому магазині</b> — місці, де зручність і вигода завжди поруч!

🛍️ <b>Для перегляду асортименту натисніть кнопку "МАГАЗИН"</b>

🚚 <b>Інформація про доставку - кнопка "ДОСТАВКА"</b>

<b>Оберіть потрібну дію з меню нижче 👇</b>
"""

# Текст для магазину
SHOP_TEXT = """
🛍️ <b>НАШ МАГАЗИН</b> 🛍️

<b>Натисніть кнопку нижче щоб перейти до повного каталогу товарів:</b>

👇 Перейдіть за посиланням для перегляду всіх товарів
"""

# Текст для доставки
DELIVERY_TEXT = """
🚚 <b>ДОСТАВКА</b>

<b>Час доставки по Україні:</b>
• Нова Пошта - 1-2 дні
• Укрпошта - 2-3 дні  
• Кур'єром по Києву - 1 день
"""

async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функція для відправки головного меню"""
    try:
        # Спершу показуємо привітальний текст
        if update.message:
            await update.message.reply_text(START_TEXT, parse_mode="HTML")
        
        # Потім головне меню з кнопками
        keyboard = [
            [InlineKeyboardButton("🛍️ МАГАЗИН", url="t.me/AppleStoreUk_bot/Shop")],
            [InlineKeyboardButton("🚚 ДОСТАВКА", callback_data="delivery")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if update.callback_query:
            await update.callback_query.edit_message_text(MAIN_MENU_TEXT, reply_markup=reply_markup, parse_mode="HTML")
        else:
            await update.message.reply_text(MAIN_MENU_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    except Exception as e:
        print(f"Помилка при відправці меню: {e}")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник команди /start"""
    await send_main_menu(update, context)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник кнопок"""
    try:
        query = update.callback_query
        await query.answer()
        
        if query.data == "delivery":
            keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back_main")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(DELIVERY_TEXT, reply_markup=reply_markup, parse_mode="HTML")
        
        elif query.data == "back_main":
            await send_main_menu(update, context)
    except Exception as e:
        print(f"Помилка в обробнику кнопок: {e}")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник текстових повідомлень - відправляє меню"""
    try:
        # Автоматично відправляємо меню при будь-якому тексті
        await send_main_menu(update, context)
    except Exception as e:
        print(f"Помилка при обробці тексту: {e}")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник помилок"""
    error = context.error
    print(f"Помилка: {error}")
    print(f"Тип помилки: {type(error)}")

def main():
    """Головна функція"""
    max_retries = 5
    retry_delay = 10  # секунд
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 Спроба запуску бота {attempt + 1}/{max_retries}...")
            
            # Створюємо додаток з таймаутами
            application = Application.builder().token(BOT_TOKEN).build()
            
            # Додаємо обробники
            application.add_handler(CommandHandler("start", start_command))
            application.add_handler(CallbackQueryHandler(button_handler))
            application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
            application.add_error_handler(error_handler)
            
            print("✅ Бот запущений і готовий до роботи!")
            print("🎯 Тепер меню з'являється автоматично!")
            print("🔄 Бот має стабільну роботу!")
            
            # Запускаємо бота
            application.run_polling(
                drop_pending_updates=True,
                allowed_updates=Update.ALL_TYPES
            )
            break
            
        except Exception as e:
            print(f"❌ Помилка при запуску (спроба {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                print(f"⏳ Чекаємо {retry_delay} секунд перед наступною спробою...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Збільшуємо затримку
            else:
                print("❌ Не вдалося запустити бота після всіх спроб")

if __name__ == "__main__":
    main()
