from typing import Final
import discord
from OpenAIConnector import get_message

TOKEN: Final[str] = 'YOUR_TOKEN'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return
    
    if client.user in message.mentions:
        await message.channel.send(get_message(message.content.replace(f'<@!{client.user.id}>', '')))
        
client.run(TOKEN)
