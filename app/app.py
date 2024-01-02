from typing import Final
import discord
from OpenAIConnector import get_message
TOKEN: Final[str] = 'NzQ1OTIxOTI5NTI1MDY3ODI2.Gabsep.JRM2x4wufgTuue1b2XH46Oi3y-s34WQnLB7-90'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:
        await message.channel.send(get_message(message.content.replace(f'<@!{client.user.id}>', '')))
        
client.run(TOKEN)
