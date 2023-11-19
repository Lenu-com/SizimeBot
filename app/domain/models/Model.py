from typing import Final, Tuple

class Model:
    def __init__(self, value: str):
        _MODELS: Final[Tuple[str]] = (
            'gpt-4',
            'gpt-3.5-turbo',
        )
        
        if value is None or value == '':
            raise ValueError('value is required.')
        
        if value not in _MODELS:
            raise ValueError('value is invalid.')
        
        self._name = value
    
    @property    
    def name(self) -> str:
        return self._name
    
    

