from state import State
class Transition:
    def __init__(self, target:State, input:set[str]):
        self.target = target
        self.input = input
    
    @property
    def target(self):
        return self.__target
    
    @target.setter
    def target(self, value:State):
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
            