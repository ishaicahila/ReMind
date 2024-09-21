from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler
from telegram import Bot, Update

from bot.handlers.commands import start, start_reminder_conversation
from bot.handlers.messages import echo, handle_reminder, cancel, handle_confirmation
from bot.config import BOT_TOKEN, CONFIRMATION, ASK_REMINDER
from bot.logger import logger
from schedule.scheduler import initialize_scheduler
from schedule import init_db

logger.info("initializing app")
application = Application.builder().token(BOT_TOKEN).build()

logger.info("initialize scheduler")
job_scheduler = initialize_scheduler()

logger.info("initializing database")
init_db


def main() -> None: 
    logger.info("adding handlers")
    application.add_handler(CommandHandler("start", start))
    application.bot_data["job_scheduler"] = job_scheduler

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("remind", start_reminder_conversation)], 
        states = {
            ASK_REMINDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reminder)],
            CONFIRMATION: [CallbackQueryHandler(handle_confirmation)]
        },
        fallbacks= [MessageHandler(filters.TEXT & ~filters.COMMAND, cancel)]

    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


    logger.info("runing polling")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()