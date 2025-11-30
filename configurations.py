import discord
import google.generativeai as genai
from discord.ext import commands
from google.generativeai.types import GenerationConfig

from load_environmentals import GEMINI_API_KEY, INSTRUCTIONS, MODEL


genai.configure(api_key=GEMINI_API_KEY)
generation_config = GenerationConfig(
    temperature=0.5,
    max_output_tokens=90,
)


model = genai.GenerativeModel(
    model_name=MODEL,
    generation_config=generation_config,
    system_instruction=INSTRUCTIONS,
)
chat_session = model.start_chat(history=[])


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
