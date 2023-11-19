import abc
from domain.models.Message import Message

class IOpenAIConnecter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def message_request(self, message: Message) -> None:
        raise NotImplementedError()
    
    