import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import random

# BOT TOKENINGIZNI BU YERGA YOZING
TOKEN = "8054125946:AAFn86bsO0_gcXpEBF6cvlQe3GJ02qmWx-4"
bot = telebot.TeleBot(TOKEN)

# 1. ASOSIY MENYU
def menu_main():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("Biz haqimizda ℹ️", callback_data="about"))
    keyboard.row(InlineKeyboardButton("O'yinlar 🎮", callback_data="game"))
    keyboard.row(InlineKeyboardButton("Buzishlik (Hacking) 💻", callback_data="hacking"))
    # Ijtimoiy tarmoqlar uchun tugmalar
    keyboard.row(
        InlineKeyboardButton("Telegram ✈️", url="https://t.me/barsabot01"),
        InlineKeyboardButton("Instagram 📸", url="instagram.com")
    )
    return keyboard

# 2. O'YINLAR MENYUSI
def game_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Tosh-Qaychi-Qog'oz ✂️", callback_data="game_tqq"))
    keyboard.add(InlineKeyboardButton("Sherni top (Lion) 🦁", callback_data="game_lion"))
    keyboard.add(InlineKeyboardButton("Tanga tashlash 🪙", callback_data="game_coin"))
    keyboard.add(InlineKeyboardButton("Omadli raqam (1-100) 🎲", callback_data="game_lucky"))
    keyboard.add(InlineKeyboardButton("Orqaga ⬅️", callback_data="back_to_main"))
    return keyboard

# --- O'YINLAR UCHUN TUGMALAR ---

def tqq_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("Tosh 🪨", callback_data="tqq_tosh"),
        InlineKeyboardButton("Qaychi ✂️", callback_data="tqq_qaychi"),
        InlineKeyboardButton("Qog'oz 📄", callback_data="tqq_qogoz")
    )
    keyboard.add(InlineKeyboardButton("Orqaga ⬅️", callback_data="game"))
    return keyboard

def lion_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("1-Eshik 🚪", callback_data="lion_1"),
        InlineKeyboardButton("2-Eshik 🚪", callback_data="lion_2"),
        InlineKeyboardButton("3-Eshik 🚪", callback_data="lion_3")
    )
    keyboard.add(InlineKeyboardButton("Orqaga ⬅️", callback_data="game"))
    return keyboard

def coin_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("Burgut 🦅", callback_data="coin_eagle"),
        InlineKeyboardButton("Panjara 🧱", callback_data="coin_tails")
    )
    keyboard.add(InlineKeyboardButton("Orqaga ⬅️", callback_data="game"))
    return keyboard

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Assalomu alaykum, {message.from_user.first_name}! Tanlang👇", reply_markup=menu_main())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id
    
    # MENYULAR NAVIGATSIYASI
    if call.data == "game":
        bot.edit_message_text("Qaysi o'yinni o'ynaymiz? 🎮", chat_id, msg_id, reply_markup=game_menu())

    elif call.data == "back_to_main":
        bot.edit_message_text("Asosiy menyu👇", chat_id, msg_id, reply_markup=menu_main())

    elif call.data == "about":
        text = ("👤 **Dasturchi haqida**\n\n"
                "🤖 Bot nomi: BARSABOT\n"
                "📅 Yil: 2025\n"
                "📸 Instagram: [turda1lovl7](instagram.com)\n"
                "✈️ Telegram: @barsabot01")
        bot.edit_message_text(text, chat_id, msg_id, reply_markup=menu_main(), parse_mode="Markdown")

    # --- LION O'YINI ---
    elif call.data == "game_lion":
        bot.edit_message_text("Sher qaysi eshik ortida? Toping! 🦁", chat_id, msg_id, reply_markup=lion_menu())

    elif call.data.startswith("lion_"):
        user_choice = call.data.split("_")[1]
        lion_pos = str(random.randint(1, 3))
        text = f"Tabriklaymiz! 🎉 Sher {lion_pos}-eshikda edi." if user_choice == lion_pos else f"Afsus... 🦁 Sher {lion_pos}-eshikda edi."
        bot.edit_message_text(text, chat_id, msg_id, reply_markup=lion_menu())

    # --- TOSH-QAYCHI-QOGOZ ---
    elif call.data == "game_tqq":
        bot.edit_message_text("Tosh-Qaychi-Qog'oz! Tanlang:", chat_id, msg_id, reply_markup=tqq_menu())

    elif call.data.startswith("tqq_"):
        user_choice = call.data.split("_")[1]
        choices = ["tosh", "qaychi", "qogoz"]
        bot_choice = random.choice(choices)
        
        if user_choice == bot_choice: result = "Durrang! 🤝"
        elif (user_choice == "tosh" and bot_choice == "qaychi") or \
             (user_choice == "qaychi" and bot_choice == "qogoz") or \
             (user_choice == "qogoz" and bot_choice == "tosh"): result = "Siz yutdingiz! 🫵🏻 🎉"
        else: result = "Bot yutdi! 🤖"
        
        bot.edit_message_text(f"Siz: {user_choice} | Bot: {bot_choice}\nNatija: {result}", chat_id, msg_id, reply_markup=tqq_menu())

    # --- TANGA TASHLAH ---
    elif call.data == "game_coin":
        bot.edit_message_text("Tanga tashlaymiz! Nima tushadi?", chat_id, msg_id, reply_markup=coin_menu())

    elif call.data.startswith("coin_"):
        result = random.choice(["eagle", "tails"])
        user_side = call.data.split("_")[1]
        win_text = "To'g'ri topdingiz! 🏆" if user_side == result else "Topolmadingiz. 😬"
        side_name = "Burgut 🦅" if result == "eagle" else "Panjara 🧱"
        bot.edit_message_text(f"Tanga tushdi: {side_name}\n{win_text}", chat_id, msg_id, reply_markup=coin_menu())

    # --- OMADLI RAQAM ---
    elif call.data == "game_lucky":
        num = random.randint(1, 100)
        bot.edit_message_text(f"Sizning omadli raqamingiz: {num} 🎲\n\nYana bitta raqam olasizmi?", chat_id, msg_id, reply_markup=game_menu())

    elif call.data == "hacking":
        bot.edit_message_text("Tizim buzilmoqda... 0% ⏳", chat_id, msg_id)
        bot.answer_callback_query(call.id, "Tizmda nosozlik 📲", show_alert=True)
        bot.answer_callback_query(call.id, "Hazillashdik! 😂", show_alert=True)
        bot.edit_message_text("Asosiy menyu👇", chat_id, msg_id, reply_markup=menu_main())

print("Bot ishga tushdi...")
bot.infinity_polling()
