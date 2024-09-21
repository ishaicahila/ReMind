from telegram.ext import Application
from bot.config import BOT_TOKEN

async def send_reminder(chat_id, text):
     application = Application.builder().token(BOT_TOKEN).build()
     await application.bot.send_message(chat_id, f"**{text}**", parse_mode='MarkdownV2')

