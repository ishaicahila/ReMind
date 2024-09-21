from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_PATH = 'reminders.db'
ASK_REMINDER = 1
CONFIRMATION = 2