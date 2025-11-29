import os

import discord.opus
import google.generativeai as genai
from discord.ext import commands
from dotenv import load_dotenv
from google.generativeai.types import GenerationConfig

discord.opus.load_opus("/opt/homebrew/opt/opus/lib/libopus.dylib")

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL")
INSTRUCTIONS = os.getenv("AI_BEHAVIOUR")
ERROR_MESSAGE = os.getenv("ERROR_MESSAGE")

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


@bot.event
async def on_ready():
    print(f"Logged as: {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        user_message = message.content.replace(f"<@{bot.user.id}>", "").strip()

        try:
            response = chat_session.send_message(user_message)

            reply_text = response.text

            await message.channel.send(reply_text)

        except Exception as e:
            message.channel.send(ERROR_MESSAGE)

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
