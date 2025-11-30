from configurations import bot, chat_session
from load_environmentals import DISCORD_TOKEN, ERROR_MESSAGE


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
