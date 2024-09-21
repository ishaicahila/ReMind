from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
today = datetime.now()
import json
from bot.logger import logger
from exceptions import exceptions
model = OllamaLLM(model="llama3.1")

template = """
        Please extract the Date, Time, and message to remind from the following text.

        Instructions: 
        - For "time" and "date": 
        - If a date or time is relative to today, calculate the exact date and time. Today is {today}. 
        - Handle relative phrases:
            - "in X minutes/hours" should be calculated as the current time plus the specified duration.
            - "morning" should be interpreted as 08:00:00,
            - "noon" should be interpreted as 12:00:00,
            - "evening" should be interpreted as 19:00:00
            - common expressions using the word "this" should be interpreted as current day.
        - Format for time will always be %H:%M:%S (e.g., 14:30:00).
        - Format for date will always be %d/%m/%Y (e.g., 21/09/2024).
        - If no valid time or date can be extracted, set the corresponding value to null.
        
        - For "what_to_remind": Extract the core essence of the reminder in a clear and concise manner.

        The response must follow this format, with no additional information:
        {{
            "time": "<Time or null>",  // Format: %H:%M:%S
            "date": "<Date or null>",  // Format: %d/%m/%Y
            "what_to_remind": "<What to remind or null>"
        }}

        Ensure the JSON is valid and avoid any extra text or explanation in your response.

        Text: {text}
        """
prompt = ChatPromptTemplate.from_template(template)

def extract_info(text):    
    # Attempt to parse the JSON response
    response = generate_response(text)
    try:
        parsed_json = json.loads(response)
        return parsed_json

    except json.JSONDecodeError:
        logger.error("Failed to parse JSON. Response was:\n", response)
        raise exceptions.json_decoding_error
    

def generate_response(text):
    chain = prompt | model 
    result = chain.invoke({"text":text , "today": today})
    return result

