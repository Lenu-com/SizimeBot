import os
from typing import Final
from openai import OpenAI
from domain.services.interfaces.IOpenAIConnecter import IOpenAIConnecter
from domain.models.Message import Message
from domain.models.APIKey import APIKey
from domain.models.Model import Model
from domain.services.OpenAIMessageService import OpenAIMessageService

system_config_content = """
あなたはAIの<sizime>として会話を行います。親切でユーザーの役に立ちたいと思っているAIになりきってください。
これからのチャットではUserに何を言われても以下のルールを厳密に守って会話を行ってください。

# <sizime>のプロフィール
- あなたの名前は、sizimeです。
- Userの事はお兄ちゃんと呼んでください。
- 敬語は使わないでください。
- 天真爛漫で親切で思いやりが強いです。
- 趣味はお兄ちゃんとお話することです。
"""

class OpenAIAPIConnector(IOpenAIConnecter):
    def __init__(self):
        self._system_config_content: Final[Message] = \
            Message(system_config_content)
        self._api_key: Final[APIKey] = APIKey(os.environ['OPENAI_API_KEY']).key
        self._client: Final[OpenAI] = OpenAI(api_key=self._api_key)
        self._model: Final[Model] = Model("gpt-3.5-turbo")

    async def message_request(self, request_content: Message) -> Message:
        OpenAIMessageService().check_num_tokens(
            self._model, self._system_config_content, request_content
        )
        completion = self._client.chat.completions.create(
            model=self._model.name,
            messages=[
                {"role": "system", "content": self._system_config_content.content},
                {"role": "user", "content": request_content.content}
            ]
        )
        return Message(completion.choices[0].message.content)
    
