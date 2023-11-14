import os
from typing import Final

import discord


TOKEN: Final[str] = os.environ['DISCORD_API_TOKEN']

class Client(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if self.user.mentioned_in(message):
            await message.channel.send(message.content)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = Client(intents=intents)
client.run(TOKEN)