from typing import Dict, Final
import tiktoken
from domain.models.Model import Model
from domain.models.Message import Message

class OpenAIMessageService:
    __TOKENS_DICT: Final[Dict[str, int]] = {
                'gpt-4-1106-preview': 128_000,
                'gpt-4-vision-preview': 128_000, 
                'gpt-4': 8_192,
                'gpt-4-0314': 8_192,
                'gpt-4-0613': 8_192,
                'gpt-4-32k': 32_768,
                'gpt-4-32k-0314': 32_768,
                'gpt-4-32k-0613': 32_768,
                'gpt-3.5-turbo': 4_096,
                'gpt-3.5-turbo-16k': 16_385,
                'gpt-3.5-turbo-0301': 4_096,
                'gpt-3.5-turbo-0613': 4_096,
                'gpt-3.5-turbo-16k-0613': 16_385,
                }
    
    @classmethod    
    def __num_tokens_from_string(cls, model: Model, config_content: Message, request_content: Message) -> int:
        encoding = tiktoken.get_encoding(model.name)
        config_content_tokens = len(encoding.encode(config_content.content))
        request_content_tokens = len(encoding.encode(request_content.content))
        return config_content_tokens + request_content_tokens
    
    @classmethod
    def __can_request(cls, model: Model, total_tokens: int) -> bool:
        return total_tokens <= cls.__TOKENS_DICT[model.name]
    
    @classmethod
    def check_num_tokens(cls, model: Model, config_content: Message, request_content: Message) -> bool:
        if not cls.__can_request(cls.__num_tokens_from_string(model, config_content, request_content)):
            raise ValueError('The number of tokens exceeds the limit.')
        return True
