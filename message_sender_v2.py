import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)


def send_message(msg):
    global MESSAGE
    MESSAGE = msg
    client.run(os.getenv('TOKEN', ''))


@client.event
async def on_ready():

    subscriber = await client.fetch_user(int(os.getenv('ID', '')))
    await subscriber.send(MESSAGE)

    await client.close()
