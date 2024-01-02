import yaml
from typing import Final
from openai import OpenAI

def load_config():
    file_path = 'config.yml'
    with open(file_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config['config']

def get_message(send_prompt: str):
    API_KEY: Final[str] = 'Your OpenAI API Key'
    CONFIG: Final[str] = load_config()
    
    client = OpenAI(
        api_key=API_KEY,
    )
    
    chat_completion = client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': CONFIG},
            {'role': 'user', 'content': send_prompt}
        ],
        model="gpt-3.5-turbo",
    )
    
    return chat_completion.choices[0].message.content