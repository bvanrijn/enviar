import telegram

bot = telegram.Bot(token='213083457:AAGxNQvchf8Q_SpgvGhQrJlFMo7MaX9Mf64')

message = raw_input("Type your message and press enter to send > ")
chat_id = bot.getUpdates()[-1].message.chat_id
bot.sendMessage(chat_id=chat_id, text=message)