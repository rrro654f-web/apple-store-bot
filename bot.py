from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import os
import asyncio

# Твій токен
BOT_TOKEN = "7460415583:AAFLutgu1nva78UxleLGJcWc4BVJAH5RIzo"

# Адмін
ADMIN_USERNAME = "@berenskolov"

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

💬 <b>Адмін:</b> {admin}

<b>Оберіть потрібну дію з меню нижче 👇</b>
""".format(admin=ADMIN_USERNAME)

# Текст для магазину
SHOP_TEXT = """
🛍️ <b>НАШ МАГАЗИН</b> 🛍️

<b>Оберіть категорію товарів:</b>

👇 Натисніть на потрібну категорію нижче
"""

# Текст для доставки
DELIVERY_TEXT = """
🚚 <b>ДОСТАВКА ТА ОПЛАТА</b>

<b>📦 Доставка по Україні:</b>
• Нова Пошта - 1-2 дні
• Укрпошта - 2-3 дні  
• Кур'єром по Києву - 1 день

<b>💳 Способи оплати:</b>
• Готівка при отриманні
• Карткою онлайн
• Розстрочка на 3 місяці
"""

# Текст для кожної категорії
IPHONE_TEXT = """
📱 <b>IPHONE</b>

<b>Нові моделі:</b>
• iPhone 17 Pro Max - від 45 000 грн
• iPhone 16 Pro - від 38 000 грн  
• iPhone 15 Pro - від 32 000 грн
• iPhone 15 - від 28 000 грн

<b>Б/в техніка:</b>
• iPhone 14 Pro Max - від 25 000 грн
• iPhone 13 Pro - від 20 000 грн

<b>Для замовлення пишіть:</b> {admin}
""".format(admin=ADMIN_USERNAME)

MACBOOK_TEXT = """
💻 <b>MACBOOK</b>

<b>Нові моделі:</b>
• MacBook Pro M3 - від 60 000 грн
• MacBook Air M2 - від 45 000 грн

<b>Б/в техніка:</b>
• MacBook Pro M2 - від 40 000 грн
• MacBook Air M1 - від 30 000 грн

<b>Для замовлення пишіть:</b> {admin}
""".format(admin=ADMIN_USERNAME)

WATCH_TEXT = """
⌚ <b>APPLE WATCH</b>

<b>Нові моделі:</b>
• Apple Watch Series 9 - від 15 000 грн
• Apple Watch Ultra 2 - від 25 000 грн

<b>Б/в техніка:</b>
• Apple Watch Series 8 - від 12 000 грн

<b>Для замовлення пишіть:</b> {admin}
""".format(admin=ADMIN_USERNAME)

AIRPODS_TEXT = """
🎧 <b>AIRPODS</b>

<b>Нові моделі:</b>
• AirPods Pro 2 - від 8 000 грн
• AirPods 3 - від 5 000 грн

<b>Б/в техніка:</b>
• AirPods Pro 1 - від 6 000 грн

<b>Для замовлення пишіть:</b> {admin}
""".format(admin=ADMIN_USERNAME)

async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функція для відправки головного меню"""
    # Спершу показуємо привітальний текст
    if update.message:
        await update.message.reply_text(START_TEXT, parse_mode="HTML")
    
    # Потім головне меню з кнопками
    keyboard = [
        [InlineKeyboardButton("🛍️ МАГАЗИН", callback_data="shop")],
        [InlineKeyboardButton("🚚 ДОСТАВКА", callback_data="delivery")],
        [InlineKeyboardButton("📱 НАПИСАТИ АДМІНУ", url=f"https://t.me/{ADMIN_USERNAME[1:]}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await update.callback_query.edit_message_text(MAIN_MENU_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    else:
        await update.message.reply_text(MAIN_MENU_TEXT, reply_markup=reply_markup, parse_mode="HTML")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник команди /start"""
    await send_main_menu(update, context)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник кнопок"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "shop":
        keyboard = [
            [InlineKeyboardButton("📱 IPHONE", callback_data="iphone"),
             InlineKeyboardButton("💻 MACBOOK", callback_data="macbook")],
            [InlineKeyboardButton("⌚ APPLE WATCH", callback_data="watch"),
             InlineKeyboardButton("🎧 AIRPODS", callback_data="airpods")],
            [InlineKeyboardButton("🔙 НАЗАД ДО МЕНЮ", callback_data="back_main")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(SHOP_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "iphone":
        keyboard = [
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop"),
             InlineKeyboardButton("📱 НАПИСАТИ АДМІНУ", url=f"https://t.me/{ADMIN_USERNAME[1:]}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(IPHONE_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "macbook":
        keyboard = [
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop"),
             InlineKeyboardButton("📱 НАПИСАТИ АДМІНУ", url=f"https://t.me/{ADMIN_USERNAME[1:]}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(MACBOOK_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "watch":
        keyboard = [
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop"),
             InlineKeyboardButton("📱 НАПИСАТИ АДМІНУ", url=f"https://t.me/{ADMIN_USERNAME[1:]}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(WATCH_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "airpods":
        keyboard = [
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop"),
             InlineKeyboardButton("📱 НАПИСАТИ АДМІНУ", url=f"https://t.me/{ADMIN_USERNAME[1:]}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(AIRPODS_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "delivery":
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back_main")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(DELIVERY_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "back_main":
        await send_main_menu(update, context)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник текстових повідомлень - відправляє меню"""
    # Автоматично відправляємо меню при будь-якому тексті
    await send_main_menu(update, context)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробник помилок"""
    print(f"Помилка: {context.error}")
    # Можна додати логіку перезапуску або сповіщення адміну

def main():
    """Головна функція"""
    # Створюємо додаток
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Додаємо обробники
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Обробник для будь-яких текстових повідомлень
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    # Обробник помилок
    application.add_error_handler(error_handler)
    
    print("✅ Бот запущений і готовий до роботи!")
    print("🎯 Тепер меню з'являється автоматично!")
    print("🔄 Бот має стабільну роботу!")
    
    # Запускаємо бота з обробкою помилок
    try:
        application.run_polling()
    except Exception as e:
        print(f"Критична помилка: {e}")
        # Можна додати автоматичний перезапуск
        print("🔄 Перезапуск бота через 5 секунд...")
        asyncio.sleep(5)
        main()

if __name__ == "__main__":
    main()
