
# Telegram LLaMA Remind Bot

This project is a Telegram bot built using Python and the LangChain framework, integrated with LLaMA3 and Ollama for natural language understanding and reminder scheduling. The bot enables users to send reminder requests in natural language, which it processes and schedules for future notifications.

## Features

- **Natural Language Understanding**: Parses reminders from user messages using LLaMA and LangChain.
- **Reminder Scheduling**: Schedules reminders based on extracted date and time.
- **User Interaction**: Reads responses from users to confirm scheduled reminders.

## How It Works

1. **User Interaction**: The user sends a reminder request in natural language.
2. **Information Extraction**: The bot uses LangChain and LLaMA to extract relevant details like date, time, and message.
3. **Reminder Scheduling**: The bot schedules the reminder for the extracted time, and stores it in the SQLite3 Database. 
4. **Notification**: Sends the reminder back to the user at the scheduled time.

## Project Structure
```
telegram-llama-remind-bot/
│
├── bot/
│   ├── __init__.py           # Initializes the bot module
│   ├── config.py             # Bot configuration settings
│   ├── logger.py             # Logger setup for the bot
│   ├── main.py               # Main entry point for the bot
│   └── handlers/
│        ├── __init__.py      # Initializes the handlers module
│        ├── commands.py      # Command handlers for the bot
│        └── messages.py      # Message handlers for user interactions
│
├── engine/
│   ├── __init__.py           # Initializes the engine module
│   └── generator.py          # Handles LLaMA and LangChain interactions
│
├── exceptions/               
│   └── exceptions.py         # Custom exception definitions
│
├── schedule/
│   ├── __init__.py           # Initializes the schedule module
│   ├── scheduler.py          # Manages reminder scheduling
│   └── helpers.py            # Helper functions for scheduling
│
├── requirements.txt          # Dependencies for the project
└── README.md                 # Project documentation
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ishaicahila/telegram-llama-remind-bot.git
   cd telegram-llama-remind-bot
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Telegram bot token in a `.env` file:
   ```bash
   BOT_TOKEN=<Your Telegram Bot Token>
   ```
5. Run the bot:
   ```bash
   python bot/main.py
   ```

## Usage

1. Start a conversation with your bot on Telegram.
2. Send a message like: 
   ```
   "Remind me to call John at 3 PM tomorrow."
   ```
3. The bot will parse the request and schedule the reminder.
4. You will receive the reminder at the specified time.

## Requirements

- Python 3.8+
- Telegram Bot API
- LangChain
- LLaMA3
- Ollama

Refer to the `requirements.txt` for more details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
