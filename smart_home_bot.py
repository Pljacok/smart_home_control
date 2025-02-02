import telebot

bot = telebot.TeleBot("your-telegram-bot-token")

@bot.message_handler(commands=['light_on'])
def turn_light_on(message):
    bot.reply_to(message, "💡 Світло увімкнено!")

@bot.message_handler(commands=['light_off'])
def turn_light_off(message):
    bot.reply_to(message, "🌙 Світло вимкнено!")

bot.polling()
