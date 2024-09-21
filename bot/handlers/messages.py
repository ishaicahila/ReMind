from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, ContextTypes, ConversationHandler

from bot.logger import logger
from engine import generator 
from bot.config import ASK_REMINDER, CONFIRMATION
from schedule import scheduler 

from exceptions import exceptions


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    logger.info("echo")
    await update.message.reply_text(update.message.text)

async def handle_reminder(update: Update, context = CallbackContext) -> None: 
    try: 
        logger.info('reminder handeling')

        thinking_message = await update.message.reply_text("Thinking...")

        chat_id = update.message.chat_id
        user_message = update.message.text

        reminder_json = generator.extract_info(user_message)

        reminder_text = reminder_json.get("what_to_remind")
        reminder_time = reminder_json.get("time")
        reminder_date = reminder_json.get("date")

        context.user_data['reminder'] = {
            'text': reminder_text,
            'time': reminder_time,
            'date': reminder_date,
            'chat_id': chat_id
        }


        logger.info(reminder_json)
        keyboard = [
                [
                    InlineKeyboardButton("Yes", callback_data="confirm_yes"),
                    InlineKeyboardButton("No", callback_data="confirm_no")
                ]
            ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=thinking_message.message_id,
            text=f"I will remind you to {reminder_text} at {reminder_time} on {reminder_date}. Is that correct?",
            reply_markup=reply_markup
        )        
        return CONFIRMATION
    except exceptions.baseException as e: 
        logger.error(e.ERROR_STR)
        if not e.TERMINATE: 
            return ConversationHandler.END
            

async def handle_confirmation(update: Update, context = CallbackContext) -> None:
    logger.info('confirmation handeling')

    query= update.callback_query
    await query.answer()

    user_choice = query.data

    if (user_choice == "confirm_yes"):
        reminder = context.user_data.get('reminder')
        try: 
            id = scheduler.add_reminder(
                    reminder['text'],
                    reminder['time'],
                    reminder['date'],
                    reminder['chat_id']
                    )
            logger.info('reminder added to db')

            scheduler.schedule_reminder(id, context.bot_data["job_scheduler"])
            logger.info('reminder scheduled')

            await query.edit_message_text("Great! I have scheduled your reminder.")


            return ConversationHandler.END
        except exceptions.baseException as e: 
            logger.error(e.ERROR_STR)
            if not e.TERMINATE: 
                return ConversationHandler.END
    elif (user_choice == "confirm_no"):
        await query.edit_message_text("Okay, please provide the details again.")
        context.user_data.pop('reminder', None)
        return ASK_REMINDER

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Reminder creation canceled.")
    return ConversationHandler.END