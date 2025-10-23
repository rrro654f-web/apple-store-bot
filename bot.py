from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

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

Ми раді, що ви завітали до нас. Тут ви знайдете великий вибір продукції за привабливими цінами, а також швидкий сервіс і надійну підтримку.

🔹 <b>Щоб ознайомитися з нашим асортиментом</b>, просто натискайте кнопку "Магазин". У розділі зібрані всі актуальні пропозиції та новинки.

🔹 <b>Для вашої зручності</b> ми додали меню, яке відкривається у нижньому кутку чату. Завдяки цьому ви з легкістю знайдете інформацію про оплату, доставку та гарантії.

🔹 <b>Якщо у вас є питання</b> або потрібна допомога у виборі — пишіть нам у Instagram! Посилання на нашу сторінку є в меню.

💬 <b>Ми завжди готові допомогти</b> вам знайти саме те, що вам потрібно!

Дякуємо за ваш вибір та бажаємо приємних покупок! 💛
"""

# Текст для магазину
SHOP_TEXT = """
🛍️ <b>НАШ МАГАЗИН</b> 🛍️

<b>Оберіть категорію товарів:</b>

👇 Натисніть на потрібну категорію нижче
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
• iPhone 12 - від 15 000 грн

✅ <b>Гарантія 12 місяців</b>
✅ <b>Оригінальна техніка Apple</b>
"""

MACBOOK_TEXT = """
💻 <b>MACBOOK</b>

<b>Нові моделі:</b>
• MacBook Pro M3 - від 60 000 грн
• MacBook Air M2 - від 45 000 грн

<b>Б/в техніка:</b>
• MacBook Pro M2 - від 40 000 грн
• MacBook Air M1 - від 30 000 грн
• MacBook Pro 2020 - від 25 000 грн

✅ <b>Повна перевірка перед продажем</b>
✅ <b>Оригінальні комплектуючі</b>
"""

WATCH_TEXT = """
⌚ <b>APPLE WATCH</b>

<b>Нові моделі:</b>
• Apple Watch Series 9 - від 15 000 грн
• Apple Watch Ultra 2 - від 25 000 грн

<b>Б/в техніка:</b>
• Apple Watch Series 8 - від 12 000 грн
• Apple Watch Series 7 - від 10 000 грн

✅ <b>Оригінальні ремінці в наявності</b>
✅ <b>Повна комплектація</b>
"""

AIRPODS_TEXT = """
🎧 <b>AIRPODS</b>

<b>Нові моделі:</b>
• AirPods Pro 2 - від 8 000 грн
• AirPods 3 - від 5 000 грн
• AirPods 2 - від 3 500 грн

<b>Б/в техніка:</b>
• AirPods Pro 1 - від 6 000 грн
• AirPods 2 - від 2 500 грн

✅ <b>Оригінальні зарядні кейси</b>
✅ <b>Перевірка звуку перед продажем</b>
"""

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Спершу показуємо привітальний текст
    await update.message.reply_text(START_TEXT, parse_mode="HTML")
    
    # Потім головне меню з кнопками
    keyboard = [
        [InlineKeyboardButton("🛍️ МАГАЗИН", callback_data="shop")],
        [InlineKeyboardButton("📱 INSTAGRAM", url="https://instagram.com/your_profile"),
         InlineKeyboardButton("📞 КОНТАКТИ", callback_data="contacts")],
        [InlineKeyboardButton("🚚 ДОСТАВКА", callback_data="delivery"),
         InlineKeyboardButton("💬 ДОПОМОГА", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(MAIN_MENU_TEXT, reply_markup=reply_markup, parse_mode="HTML")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
            [InlineKeyboardButton("🛒 ЗАМОВИТИ IPHONE", url="https://t.me/your_username")],
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(IPHONE_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "macbook":
        keyboard = [
            [InlineKeyboardButton("🛒 ЗАМОВИТИ MACBOOK", url="https://t.me/your_username")],
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(MACBOOK_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "watch":
        keyboard = [
            [InlineKeyboardButton("🛒 ЗАМОВИТИ APPLE WATCH", url="https://t.me/your_username")],
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(WATCH_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "airpods":
        keyboard = [
            [InlineKeyboardButton("🛒 ЗАМОВИТИ AIRPODS", url="https://t.me/your_username")],
            [InlineKeyboardButton("🔙 НАЗАД ДО МАГАЗИНУ", callback_data="shop")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(AIRPODS_TEXT, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "contacts":
        contacts_text = """
📞 <b>НАШІ КОНТАКТИ</b>

<b>Телефон:</b> +380 (XX) XXX-XX-XX
<b>Email:</b> info@applestore.ua  
<b>Адреса:</b> м. Київ, вул. Примерна, 1

<b>Графік роботи:</b>
🕘 Пн-Пт: 9:00-20:00
🕙 Сб-Нд: 10:00-18:00

<b>Ми завжди на зв'язку! 📲</b>
"""
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back_main")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(contacts_text, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "delivery":
        delivery_text = """
🚚 <b>ДОСТАВКА ТА ОПЛАТА</b>

<b>📦 Доставка по Україні:</b>
• Нова Пошта - 1-2 дні
• Укрпошта - 2-3 дні  
• Кур'єром по Києву - 1 день

<b>💳 Способи оплати:</b>
• Готівка при отриманні
• Карткою онлайн
• Розстрочка на 3 місяці

<b>🔒 Гарантія:</b> 12 місяців на всю техніку
<b>🔄 Повернення:</b> 14 днів з моменту отримання

<b>Все швидко, зручно та безпечно! ✅</b>
"""
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back_main")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(delivery_text, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "help":
        help_text = """
💬 <b>ДОПОМОГА</b>

<b>Як зробити замовлення?</b>
1. Перейдіть у "Магазин"
2. Оберіть потрібну категорію
3. Натисніть "Замовити"
4. Напишіть нам у дірект

<b>Потрібна допомога?</b>
📞 Телефон: +380 (XX) XXX-XX-XX
📱 Instagram: @your_profile

<b>Ми завжди раді допомогти! 😊</b>
"""
        keyboard = [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back_main")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(help_text, reply_markup=reply_markup, parse_mode="HTML")
    
    elif query.data == "back_main":
        keyboard = [
            [InlineKeyboardButton("🛍️ МАГАЗИН", callback_data="shop")],
            [InlineKeyboardButton("📱 INSTAGRAM", url="https://instagram.com/your_profile"),
             InlineKeyboardButton("📞 КОНТАКТИ", callback_data="contacts")],
            [InlineKeyboardButton("🚚 ДОСТАВКА", callback_data="delivery"),
             InlineKeyboardButton("💬 ДОПОМОГА", callback_data="help")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(MAIN_MENU_TEXT, reply_markup=reply_markup, parse_mode="HTML")

def main():
    application = Application.builder().token("7460415583:AAFLutgu1nva78UxleLGJcWc4BVJAH5RIzo").build()
    
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("✅ Бот запущений і готовий до роботи!")
    print("🔧 Тепер бот має зручне меню та красиві тексти!")
    application.run_polling()

if __name__ == "__main__":
    main()
