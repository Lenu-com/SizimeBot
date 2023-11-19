class APIKey:
    def __init__(self, value: str):
        if value is None or value == '':
            raise ValueError('value is required.')
        self.__key = value
        
    @property
    def key(self) -> str:
        return self.__key
    