class Transition:
    def __init__(self, target:str, input:set[str]):
        self.target = target
        self.input = input
    
    def __str__(self):
        return f'on input <{self.input}> -> {self.target.label}'

    @property
    def target(self):
        return self.__target
    
    @target.setter
    def target(self, value:str):
        valid = True
        if(valid):
            self.__target = value
        else:
            raise ValueError(f'Invalid target state')
    
    @property
    def input(self):
        return self.__input
    
    @input.setter
    def input(self, value:set[str]):
        valid = True
        if(valid):
            self.__input = value
        else:
            raise ValueError(f'Invalid input char')
            