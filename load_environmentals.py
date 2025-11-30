import os

from dotenv import load_dotenv

load_dotenv()
# Needed for Bot to work
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL")

# Not Needed, but recommended for better experience
INSTRUCTIONS = os.getenv("AI_BEHAVIOUR")
ERROR_MESSAGE = os.getenv("ERROR_MESSAGE", "API Error")
