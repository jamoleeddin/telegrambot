from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Assalomu alaykum, botga xush kelibsiz!")

def main():
    updater = Updater(token="6176149316:AAHY2J8lXvRZFjXFwLgvVhFv-5HXicvhErE", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
