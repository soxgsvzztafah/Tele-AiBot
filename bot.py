import logging
from telegram.ext import Updater, MessageHandler, Filters
from config import BOT_TOKEN

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the echo function
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main():
    # Create an Updater object and connect it to your bot token
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the echo function as a message handler
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C to stop it
    updater.idle()

if __name__ == '__main__':
    main()