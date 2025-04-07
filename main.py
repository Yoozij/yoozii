
import os
import telebot
import openai

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
openai.api_key = os.getenv("OPENAI_API_KEY")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response.choices[0].message.content)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()
