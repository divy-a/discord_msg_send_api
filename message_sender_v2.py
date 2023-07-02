import discord
import os
from dotenv import load_dotenv

load_dotenv()


def new_client():
    return discord.Client(intents=discord.Intents.default())


def send_message(msg):
    client = new_client()

    @client.event
    async def on_ready():
        subscriber = await client.fetch_user(int(os.getenv('ID', '')))
        await subscriber.send(msg)

        await client.close()

    client.run(os.getenv('TOKEN', ''))
