import os
from typing import Final
import discord
from domain.services.interfaces.IDiscordAPIConnecter import IDiscordAPIConnecter
from domain.models.APIKey import APIKey

class DiscordAPIConncter(discord.Client, IDiscordAPIConnecter):
    __API_KEY: Final[APIKey] = APIKey(os.environ['DISCORD_API_KEY'])
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if self.user.mentioned_in(message):
            await message.channel.send(message.content)
            
    

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = DiscordAPIConncter(intents=intents)
client.run(client.__API_KEY.key)