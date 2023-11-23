from django.core.management.base import BaseCommand
import telebot
from app.models import News

bot = telebot.TeleBot("6686148336:AAHZeZmP09XxF6KOs_mO_nslxS1KJaMvJ9k")  # Вставьте сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['news'])
def get_news(message):
    news_list = News.objects.all()
    if news_list:
        for news_item in news_list:
            message_text = f"{news_item.title}\n\n{news_item.content}\n\nPublished on: {news_item.pub_date}"
            bot.send_message(message.chat.id, message_text)
    else:
        bot.send_message(message.chat.id, "No news available.")

@bot.message_handler(commands=['help'])
def show_help(message):
    commands_list = [
        "/start - старт бота",
        "/news - список новостей",
        "/help - команды",
        "/add <newstitle> <content> - добавить новость",
    ]
    bot.send_message(message.chat.id, "\n".join(commands_list))

@bot.message_handler(commands=['add'])
def add_news(message):
    try:
        _, title, content = message.text.split(' ', 2)
        News.objects.create(title=title, content=content)
        bot.send_message(message.chat.id, "News added successfully!")
    except ValueError:
        bot.send_message(message.chat.id, "Invalid format. Use /add <newstitle> <content>")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
