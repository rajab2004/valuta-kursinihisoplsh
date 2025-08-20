from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from .config import BOT_TOKEN
from .states import States
from .handlers import start, menu, som_to_usd, usd_to_som, cancel

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            States.MENU: [MessageHandler(Filters.text & ~Filters.command, menu)],
            States.SUM_TO_USD: [MessageHandler(Filters.text & ~Filters.command, som_to_usd)],
            States.USD_TO_SUM: [MessageHandler(Filters.text & ~Filters.command, usd_to_som)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        name="currency_conv",
        persistent=False,
    )

    dp.add_handler(conv)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
