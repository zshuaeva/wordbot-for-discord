import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

allowed_channel_id = "channel_id"


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if (
        message.channel.id == allowed_channel_id
        and "word trigger here" in message.content.lower()
    ):
        await message.channel.send("Response to word trigger")

    await bot.process_commands(message)


bot.run("bot_key")
