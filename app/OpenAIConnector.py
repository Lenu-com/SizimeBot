import yaml
from typing import Final
from openai import OpenAI
import tiktoken

def load_config():
    file_path = 'config.yml'
    with open(file_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config['config']

MODEL: Final[str] = 'gpt-3.5-turbo'
TOKEN_MAX: Final[int] = 4096
API_KEY: Final[str] = 'YOUR_OPENAI_API_KEY'
CONFIG: Final[str] = load_config()

def is_token_over(message: str):
    encode = tiktoken.encoding_for_model(MODEL)
    config_token = encode.encode(CONFIG)
    message_token = encode.encode(message)
    total_token = len(config_token) + len(message_token)
    return total_token > TOKEN_MAX


def get_message(message: str):
    client = OpenAI(
        api_key=API_KEY,
    )
    
    if is_token_over(message):
        message = 'メッセージが長すぎます。とUserに送信してください。'
    
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': CONFIG},
            {'role': 'user', 'content': message}
        ],
        model=MODEL,
    )
    
    return chat_completion.choices[0].message.content
