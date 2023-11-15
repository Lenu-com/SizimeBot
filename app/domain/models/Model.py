from typing import Final, Tuple

class Model:
    def __init__(self, value: str):
        __MODELS: Final[Tuple[str]] = (
                'gpt-4-1106-preview',
                'gpt-4-vision-preview',
                'gpt-4',
                'gpt-4-0314',
                'gpt-4-0613',
                'gpt-4-32k',
                'gpt-4-32k-0314',
                'gpt-4-32k-0613',
                'gpt-3.5-turbo',
                'gpt-3.5-turbo-16k',
                'gpt-3.5-turbo-0301',
                'gpt-3.5-turbo-0613',
                'gpt-3.5-turbo-16k-0613',
        )
        
        if value is None or value == '':
            raise ValueError('value is required.')
        
        if value not in __MODELS:
            raise ValueError('value is invalid.')
        
        self.__name = value
    
    @property    
    def name(self) -> str:
        return self.__name