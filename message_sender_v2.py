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

        except Exception as ex:
            print(ex)

        
        await client.close()
        if not client.is_closed():
            try:
                exit()
            except:
                pass
        
    
    client.run(os.getenv('TOKEN', ''))
