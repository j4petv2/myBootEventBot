import telegram
# from telegram import update

chat_token = "1434416550:AAE9OeHYuL8mHxxspfxKQCNUoFS1vrtlZ7Q"
bot = telegram.Bot(token=chat_token)
updates = bot.getUpdates()

print(updates)

for i in updates:
    print(i)

print("start telegram bot")
