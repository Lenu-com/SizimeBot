import abc
import discord

class IDiscordAPIConnecter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def on_message(self, message: discord.Message) -> discord.Message:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def send_message(self, message: discord.Message) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def is_mentioned(self, message: discord.Message) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def is_me(self, message: discord.Message) -> bool:
        raise NotImplementedError()
    