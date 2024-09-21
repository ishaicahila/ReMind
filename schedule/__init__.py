import sqlite3
import os
from bot.logger import logger
from bot.config import DB_PATH

def init_db():
    if not os.path.exists(DB_PATH):
        # Create the db
        connection = sqlite3.connect(DB_PATH)

        # Create the cursor obj
        cursor = connection.cursor()


        cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    chat_id INTEGER NOT_NULL, 
                    reminder_message TEXT NOT_NULL, 
                    reminder_time TIMESTAMP NOT NULL)
                    ''')

        connection.commit()
        connection.close()
        

