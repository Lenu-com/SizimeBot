import discord
from infrastructure.DiscordAPIConnector import DiscordAPIConnector

def main():
    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True
    client = DiscordAPIConnector(intents=intents)
    client.run(client._api_key)

if __name__ == "__main__":
    main()
    