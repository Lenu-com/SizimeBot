import os
from openai import OpenAI
from typing import Final
from domain.services.interfaces.IOpenAIConnecter import IOpenAIConnecter
from domain.models.Message import Message
from domain.models.APIKey import APIKey
from domain.models.Model import Model
from domain.services.OpenAIMessageService import OpenAIMessageService

class OpenAIAPIConnector(IOpenAIConnecter):
    def __init__(self):
        self.__SYSTEM_CONFIG_CONTENT: Final[Message] = \
            Message('''
                    ''')
        self.__API_KEY: Final[APIKey] = APIKey(os.environ['OPENAI_API_KEY']).key
        self.__CLIENT: Final[OpenAI] = OpenAI(api_key=self.__API_KEY)
        self.__MODEL: Final[Model] = Model("gpt-3.5-turbo-1106")

    def message_request(self, request_content: Message) -> Message:
        OpenAIMessageService().check_num_tokens(self.__MODEL, self.__SYSTEM_CONFIG_CONTENT, request_content)
        completion = self.__CLIENT.chat.completions.create(
            model = self.__MODEL.name,
            messages=[
                {"role": "system", "content": self.__SYSTEM_CONFIG_CONTENT},
                {"role": "user", "content": request_content}
                ]
        )
        return Message(completion.choices[0].message.content)