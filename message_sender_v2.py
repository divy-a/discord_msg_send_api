import discord
import os
from dotenv import load_dotenv


def send_message(msg):
    load_dotenv()

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():

        try:
            subscriber = await client.fetch_user(int(os.getenv('ID', '')))
            await subscriber.send(msg)

        except:
            pass

        await client.close()
        #exit()

    client.run(os.getenv('TOKEN', ''))
