from model.transition import Transition
class State:
    def __init__(self, label:str, transitions:set[Transition] = {}):
        self.label:str = label
        self.transitions:set[Transition] = transitions
    
    @property
    def label(self):
        return self.__label
    
    @label.setter
    def label(self, value:str):
        valid = True
        if(valid):
            self.__label = value
        else:
            raise ValueError(f'Invalid state name')

    @property
    def transitions(self):
        return self.__transitions
    
    @transitions.setter
    def transitions(self, value:Transition):
        valid = True
        if(valid):
            self.__transitions = value
        else:
            raise ValueError(f'invalid state transition')

