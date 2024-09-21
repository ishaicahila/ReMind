
# Telegram LLaMA Reminder Bot

This is a Telegram bot that allows users to set reminders using natural language commands. The bot leverages the LLaMA language model to understand and parse user inputs for setting reminders. It is designed to recognize the time, date, and content of the reminder from a user's message and then schedule it accordingly.

## Features

- **Natural Language Processing**: Utilizes LLaMA and LangChain for parsing natural language inputs.
- **Reminders**: Allows users to schedule reminders that the bot will send back to them at the specified time.
- **Flexible Scheduling**: Supports different formats for specifying date and time.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A Telegram bot token (create one using the [BotFather](https://core.telegram.org/bots#botfather) on Telegram).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ishaicahila/telegram-llama-remind-bot.git
   cd telegram-llama-remind-bot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot token:

   Create a `.env` file in the root directory of the project and add your Telegram bot token:

   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```

## Usage

- Start a chat with your bot on Telegram.
- Send a message with a reminder request, e.g., "Remind me to call John tomorrow at 10 AM."
- The bot will confirm the reminder and notify you at the specified time.

## Project Structure

- `bot.py`: The main bot script that handles incoming messages and sets reminders.
- `reminder_handler.py`: Contains the logic for parsing messages and scheduling reminders.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `README.md`: This file, containing information about the project and how to use it.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
