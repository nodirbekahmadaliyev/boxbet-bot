import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- BOT VA KANAL SOZLAMALARI ---
TOKEN = "8231087400:AAFsH6Y0T1STUysr-AyUVLGLC0cQV0eTcmg"
CHANNEL_ID = -1002546569165  # sizning yopiq kanal ID
bot = telebot.TeleBot(TOKEN)

# --- /start KOMANDASI ---
@bot.message_handler(commands=['start'])
def start_msg(message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🇺🇿 O‘zbek", callback_data="lang_uz"),
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")
    )
    bot.send_message(message.chat.id, "Tilni tanlang / Выберите язык:", reply_markup=keyboard)

# --- TIL TANLASH ---
@bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
def set_lang(call):
    lang = call.data.split("_")[1]
    chat_id = call.message.chat.id

    keyboard = InlineKeyboardMarkup(row_width=1)
    if lang == "uz":
        keyboard.add(
            InlineKeyboardButton("🔵 1XBET yuklash", callback_data="apk_1xbet"),
            InlineKeyboardButton("🟢 WinWin yuklash", callback_data="apk_winwin"),
            InlineKeyboardButton("🟡 Melbet yuklash", callback_data="apk_melbet")
        )
        bot.send_message(chat_id, "Ilovani tanlang:", reply_markup=keyboard)
    else:
        keyboard.add(
            InlineKeyboardButton("🔵 1XBET Скачать", callback_data="apk_1xbet"),
            InlineKeyboardButton("🟢 WinWin Скачать", callback_data="apk_winwin"),
            InlineKeyboardButton("🟡 Melbet Скачать", callback_data="apk_melbet")
        )
        bot.send_message(chat_id, "Выберите приложение:", reply_markup=keyboard)

# --- APK TUGMALARINI BOSISH ---
@bot.callback_query_handler(func=lambda call: call.data.startswith("apk_"))
def send_apk(call):
    apk_key = call.data.split("_")[1]

    # Kanalga joylangan APK xabarlarining ID'lari
    apk_ids = {
        "1xbet": 5,   # 1XBET APK xabar ID
        "winwin": 4,  # WinWin APK xabar ID
        "melbet": 3   # Melbet APK xabar ID
    }

    if apk_key in apk_ids:
        bot.copy_message(call.message.chat.id, CHANNEL_ID, apk_ids[apk_key])
    else:
        bot.send_message(call.message.chat.id, "Bu APK hali kanalga yuklanmagan.")

# --- BOTNI ISHGA TUSHIRISH ---
bot.infinity_polling()