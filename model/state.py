from model.transition import Transition
class State:
    def __init__(self, label:str, transitions = set()):
        self.label:str = label
        self.transitions = transitions
    
    def add_transition(self, input:str, target):
        self.transitions.add(Transition(input=input, target=target))

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

