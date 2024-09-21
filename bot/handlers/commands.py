from telegram import Update, ForceReply
from telegram.ext import CommandHandler, CallbackContext, ContextTypes

from bot.logger import logger
from bot.config import ASK_REMINDER, CONFIRMATION

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    logger.info('start')
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def start_reminder_conversation(update: Update, context = CallbackContext) -> None: 
    logger.info('start reminder conversation')
    await update.message.reply_text("What would you like me to remind you and when ? ")
    return ASK_REMINDER