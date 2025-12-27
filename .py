import os  # Bu yerga qo'shiladi
import telebot
import random
import time
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import time

# BOT TOKENINGIZ
TOKEN = "8054125946:AAFn86bsO0_gcXpEBF6cvlQe3GJ02qmWx-4"
bot = telebot.TeleBot(TOKEN)

# 1. ASOSIY MENYU
def menu_main():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🎮 O'yinlar menyusi", callback_data="game"))
    keyboard.add(InlineKeyboardButton("ℹ️ Biz haqimizda", callback_data="about"))
    keyboard.add(InlineKeyboardButton("💻 Hacking (Hazil)", callback_data="hacking"))
    keyboard.row(
        InlineKeyboardButton("✈️ Telegram", url="t.me"),
        InlineKeyboardButton("📸 Instagram", url="instagram.com")
    )
    return keyboard

# 2. O'YINLAR MENYUSI
def game_menu():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("✂️ Tosh-Qaychi", callback_data="game_tqq"),
        InlineKeyboardButton("🦁 Sherni top", callback_data="game_lion"),
        InlineKeyboardButton("🪙 Tanga tashlash", callback_data="game_coin"),
        InlineKeyboardButton("🎲 Omadli raqam", callback_data="game_lucky"),
        InlineKeyboardButton("🐍 Snake (PC uchun)", callback_data="game_snake") # YANGI
    )
    keyboard.add(InlineKeyboardButton("⬅️ Orqaga", callback_data="back_to_main"))
    return keyboard

# --- COMMAND HANDLERS ---
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id, 
        f"Assalomu alaykum, {message.from_user.first_name}! **BARSABOT**-ga xush kelibsiz! 👇", 
        reply_markup=menu_main(),
        parse_mode="Markdown"
    )

# --- CALLBACK HANDLERS ---
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    
    if call.data == "back_to_main":
        bot.edit_message_text("Asosiy menyu👇", chat_id, msg_id, reply_markup=menu_main())

    elif call.data == "game":
        bot.edit_message_text("O'yinni tanlang: 🎮", chat_id, msg_id, reply_markup=game_menu())

    # SNAKE O'YINI UCHUN JAVOB
    elif call.data == "game_snake":
        snake_info = (
            "🐍 **Snake Game (Iloncha)**\n\n"
            "Bu o'yin grafikali bo'lgani uchun uni Telegram ichida o'ynab bo'lmaydi.\n\n"
            "💻 Uni kompyuteringizda ishga tushirish uchun Python o'rnatilgan bo'lishi kerak.\n"
            "Kodni GitHub-dan yuklab oling yoki dasturchidan so'rang!"
        )
        back_btn = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Orqaga", callback_data="game"))
        bot.edit_message_text(snake_info, chat_id, msg_id, reply_markup=back_btn, parse_mode="Markdown")

    elif call.data == "hacking":
        # 1. Avval foydalanuvchiga bildirishnoma yuboramiz
        bot.answer_callback_query(call.id, "Tizim buzildi! Kompyuter restart qilinmoqda...", show_alert=True)
        time.sleep(5)
        # 2. Telegram xabarni o'zgartiramiz
        bot.edit_message_text("⚠️ DIQQAT: Kompyuter o'chirilmoqda...", chat_id, msg_id)
        time.sleep(5)
        # 3. Va kompyuterga restart buyrug'ini yuboramiz
        os.system("shutdown /r /t 0")


    elif call.data == "about":
        about_text = "👤 **Dasturchi:** @barsabot01\n📅 **Yil:** 2025\n\nBarcha o'yinlar Python tilida yozilgan."
        back_btn = InlineKeyboardMarkup().add(InlineKeyboardButton("⬅️ Orqaga", callback_data="back_to_main"))
        bot.edit_message_text(about_text, chat_id, msg_id, reply_markup=back_btn, parse_mode="Markdown")

    elif call.data == "hacking":
        # Vizual aldash effekti
        bot.edit_message_text("📡 Serverga ulanish o'rnatilmoqda...", chat_id, msg_id)
        time.sleep(1)
        bot.edit_message_text("🔓 Parollar buzilmoqda: 25%...", chat_id, msg_id)
        time.sleep(1)
        bot.edit_message_text("📂 Shaxsiy rasmlar ko'chirilmoqda: 60%...", chat_id, msg_id)
        time.sleep(1)
        bot.edit_message_text("🛑 Tizim aniqlandi! IP: 192.168.1.1", chat_id, msg_id)
        time.sleep(1)
        
        # Oxirida hazil ekanini aytish
        bot.answer_callback_query(call.id, "Hazillashdik! 😂 BARSABOT sizning xavfsizligingizni ta'minlaydi.", show_alert=True)
        bot.edit_message_text("Asosiy menyu👇", chat_id, msg_id, reply_markup=menu_main())


    # --- O'YINLAR MANTIQI ---
    elif call.data == "game_lucky":
        num = random.randint(1, 100)
        bot.edit_message_text(f"🎲 Omadli raqamingiz: **{num}**", chat_id, msg_id, reply_markup=game_menu(), parse_mode="Markdown")

    elif call.data == "game_coin":
        res = random.choice(["Burgut 🦅", "Panjara 🧱"])
        bot.edit_message_text(f"🪙 Natija: **{res}**", chat_id, msg_id, reply_markup=game_menu(), parse_mode="Markdown")

    elif call.data == "game_tqq":
        bot_choice = random.choice(["Tosh 🪨", "Qaychi ✂️", "Qog'oz 📄"])
        bot.edit_message_text(f"Bot tanladi: {bot_choice}\n\nYana o'ynaymizmi?", chat_id, msg_id, reply_markup=game_menu())

    elif call.data == "game_lion":
        lion_pos = random.randint(1, 3)
        bot.edit_message_text(f"🦁 Sher {lion_pos}-eshikda edi! Topa oldingizmi?", chat_id, msg_id, reply_markup=game_menu())

print("Bot ishlamoqda...")
bot.infinity_polling()
