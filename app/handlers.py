from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from .states import States
from .keyboards import main_menu_kb, back_kb
from .exchange import get_usd_to_uzs_rate, ExchangeError

WELCOME_TEXT = (
    "Salom! Men sizga so'm ↔ dollar o‘tkazishda yordam beraman.\n"
    "Iltimos, menyudan tanlang 👇"
)

HELP_TEXT = (
    "Men nimalar qila olaman:\n"
    "• So'm → Dollar hisoblash\n"
    "• Dollar → So'm hisoblash\n"
    "Har safar ⬅️ Orqaga tugmasi orqali bosh menyuga qaytishingiz mumkin."
)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(WELCOME_TEXT, reply_markup=main_menu_kb())
    return States.MENU

def menu(update: Update, context: CallbackContext):
    text = (update.message.text or "").strip()
    if text == "💵 So'm → Dollar":
        update.message.reply_text(
            "So‘m miqdorini kiriting (masalan: 5000000):",
            reply_markup=back_kb()
        )
        return States.SUM_TO_USD
    elif text == "💲 Dollar → So'm":
        update.message.reply_text(
            "Dollar miqdorini kiriting (masalan: 100):",
            reply_markup=back_kb()
        )
        return States.USD_TO_SUM
    else:
        update.message.reply_text(HELP_TEXT, reply_markup=main_menu_kb())
        return States.MENU

def som_to_usd(update: Update, context: CallbackContext):
    text = (update.message.text or "").strip()
    if text == "⬅️ Orqaga":
        update.message.reply_text("Bosh menyu:", reply_markup=main_menu_kb())
        return States.MENU
    try:
        som = float(text.replace(",", "").replace(" ", ""))
        rate = get_usd_to_uzs_rate()  # USD -> UZS
        usd = som / rate
        update.message.reply_text(f"{som:,.0f} so‘m ≈ {usd:.2f} $", reply_markup=back_kb())
    except ValueError:
        update.message.reply_text("Iltimos, faqat son kiriting! (masalan: 5000000)")
    except ExchangeError as e:
        update.message.reply_text(f"Kursni olishda xatolik: {e}. Keyinroq urinib ko'ring.")
    return States.SUM_TO_USD

def usd_to_som(update: Update, context: CallbackContext):
    text = (update.message.text or "").strip()
    if text == "⬅️ Orqaga":
        update.message.reply_text("Bosh menyu:", reply_markup=main_menu_kb())
        return States.MENU
    try:
        usd = float(text.replace(",", "").replace(" ", ""))
        rate = get_usd_to_uzs_rate()  # USD -> UZS
        som = usd * rate
        update.message.reply_text(f"{usd:.2f} $ ≈ {som:,.0f} so‘m", reply_markup=back_kb())
    except ValueError:
        update.message.reply_text("Iltimos, faqat son kiriting! (masalan: 100)")
    except ExchangeError as e:
        update.message.reply_text(f"Kursni olishda xatolik: {e}. Keyinroq urinib ko'ring.")
    return States.USD_TO_SUM

def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Bot to‘xtadi.", reply_markup=ReplyKeyboardRemove())
    return -1
