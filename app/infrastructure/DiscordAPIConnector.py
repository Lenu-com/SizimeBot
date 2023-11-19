import os
from typing import Final
import discord
from domain.services.interfaces.IDiscordAPIConnecter import IDiscordAPIConnecter
from domain.models.APIKey import APIKey
from domain.models.Message import Message
from infrastructure.OpenAIAPIConnector import OpenAIAPIConnector

class DiscordAPIConnector(discord.Client, IDiscordAPIConnecter):
    _api_key: Final[APIKey] = APIKey(os.environ['DISCORD_API_KEY']).key
    
    async def on_message(self, message: discord.Message):
        if self.is_me(message):
            return
        if self.is_mentioned(message):
            await self.send_message(message)
            
    async def send_message(self, message: discord.Message) -> None:
        send_message = OpenAIAPIConnector().message_request(Message(message.content))
        await message.channel.send(send_message.content)
    
    def is_mentioned(self, message: discord.Message) -> bool:
        return self.user.mentioned_in(message)
    
    def is_me(self, message: discord.Message) -> bool:
        return message.author == self.user
    