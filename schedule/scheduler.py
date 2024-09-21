from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger
from exceptions import exceptions

import sqlite3
from bot.config import DB_PATH
from bot.logger import logger
from schedule.helpers import send_reminder
from datetime import datetime


def initialize_scheduler():
    jobstores = {
        'default' : SQLAlchemyJobStore(url='sqlite:///reminders.db')
    }
    # scheduler = BackgroundScheduler(jobstores=jobstores)
    scheduler = AsyncIOScheduler(jobstores=jobstores)
    scheduler.start()
    return scheduler

def schedule_reminder(reminder_id, scheduler):

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    logger.info(f"attemptiing to schedule reminder with id {reminder_id}")
    cursor.execute("SELECT* FROM reminders WHERE id = ?", [reminder_id])

    result = cursor.fetchone()

    if result: 
        chat_id = result[1]
        text = result[2]
        time = result[3]
        logger.info(f"scheduling reminder {text}")
        trigger = DateTrigger(time)
        scheduler.add_job(
            func=send_reminder, 
            trigger=trigger,
            args=[chat_id, text], 
            id=f"reminder_{reminder_id}"
        )
    else: 
        raise Exception(f"something went wrong trying to chedule {reminder_id}")

def add_reminder(text, time, date, chat_id):

    logger.info(f"adding reminder {text} to database")


    try:
        date = datetime.strptime(date,"%d/%m/%Y").date()
        time = datetime.strptime(time, "%H:%M:%S" ).time()
        scheduled = datetime.combine(date, time )

    except Exception as e: 
        raise exceptions.date_parsing_error
    

    try: 
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO reminders (chat_id, reminder_message, reminder_time) 
                    VALUES (?, ?, ?)
                    ''', (chat_id, text, scheduled  ))
        
        connection.commit()
        reminder_id = cursor.lastrowid
        connection.close()

        return reminder_id
    except Exception as e: 
        raise exceptions.failiure_while_inserting_to_db
