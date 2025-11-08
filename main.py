import os
import telebot
from openai import OpenAI

BOT_TOKEN = os.environ.get('BOT_TOKEN')
DEEPSEEK_KEY = os.environ.get('DEEPSEEK_API_KEY')

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 AI Bot Started!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": message.text}],
            max_tokens=2000
        )
        bot.reply_to(message, response.choices[0].message.content)
    except Exception as e:
        bot.reply_to(message, "❌ Error")

print("🤖 Bot starting...")
bot.infinity_polling()
