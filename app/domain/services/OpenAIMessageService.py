from typing import Dict, Final
import tiktoken
from domain.models.Model import Model
from domain.models.Message import Message
from domain.exceptions.exceptions import PromptException

class OpenAIMessageService:
    __TOKENS_DICT: Final[Dict[str, int]] = {
        'gpt-4': 8_192,
        'gpt-3.5-turbo': 4_096,
    }
    
    @classmethod    
    def __num_tokens_from_string(cls, model: Model, config: Message, request: Message) -> int:
        encoding = tiktoken.encoding_for_model(model.name)
        config_content_tokens = len(encoding.encode(text=config.content))
        request_content_tokens = len(encoding.encode(text=request.content))
        return config_content_tokens + request_content_tokens
    
    @classmethod
    def __can_request(cls, model: Model, total_tokens: int) -> bool:
        return total_tokens <= cls.__TOKENS_DICT[model.name]
    
    @classmethod
    def check_num_tokens(cls, model: Model, config_content: Message, request_content: Message) -> bool:
        total_tokens = cls.__num_tokens_from_string(model, config_content, request_content)
        if not cls.__can_request(model, total_tokens):
            raise PromptException('The prompt is too large.')
        return True
    
