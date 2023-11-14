import json
import os

import requests
from openai import OpenAI
from typing import Final


TOKEN: Final[str] = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=TOKEN)

SYSTEM_CONFIG_CONTENT = '''

'''

def get_content(send_content):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": SYSTEM_CONFIG_CONTENT},
            {"role": "user", "content": send_content}
            ]
    )
    return completion.choices[0].message.content