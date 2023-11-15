import abc
from domain.models.Message import Message

class IOpenAIConnecter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def on_message(self, message: Message) -> Message:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def send_message(self, message: Message) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def is_mentioned(self, message: Message) -> bool:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def is_me(self, message: Message) -> bool:
        raise NotImplementedError()