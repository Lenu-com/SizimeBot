class Message:
    def __init__(self, value: str):
        if value is None or value == '':
            raise ValueError('value is required.')
        self.__content: str = value
        
    @property
    def content(self) -> str:
        return self.__content
    