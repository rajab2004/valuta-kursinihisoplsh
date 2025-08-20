from telegram import ReplyKeyboardMarkup

def main_menu_kb():
    return ReplyKeyboardMarkup(
        [["💵 So'm → Dollar", "💲 Dollar → So'm"]],
        resize_keyboard=True
    )

def back_kb():
    return ReplyKeyboardMarkup([["⬅️ Orqaga"]], resize_keyboard=True)
