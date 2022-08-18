from abc import abstractmethod, ABC
from model.state import State
from model.transition import Transition

class Automata(ABC):
    def __init__(self, symbol_Epsilon:set[str] = set(), symbol_Q:set[State] = set(), symbol_q_0:State = None, symbol_F:set[State] = set()) -> None:
        self.symbol_Epsilon = symbol_Epsilon
        self.symbol_Q = symbol_Q
        self.symbol_q_0 = symbol_q_0
        self.symbol_F = symbol_F
        pass

    def add_state(self, label:str):
        new_state = State(label=label)
        self.symbol_Q.add(new_state)

    def del_state(self, label:str):
        del_state = {state for state in self.__symbol_Q if state.label == label}.pop()
        self.symbol_Q.remove(del_state)

    def get_states(self):
        return {state.label for state in self.__symbol_Q}

    def set_alphabet(self, alphabet:str):
        self.__symbol_Epsilon = {char for char in alphabet}

    def get_alphabet(self):
        return self.__symbol_Epsilon

    def set_inital(self, label):
        inital_state = {state for state in self.__symbol_Q if state.label == label}.pop()
        self.__symbol_q_0 = inital_state

    def get_inital(self):
        return self.__symbol_q_0

    @abstractmethod
    def transition_function(self):
        pass

    @property
    def symbol_Epsilon(self):
            return self.__symbol_Epsilon
    @symbol_Epsilon.setter
    def symbol_Epsilon(self, value:set[str]):
            valid = True
            if(valid):
                self.__symbol_Epsilon = value
            else:
                raise ValueError(f'Invalid Alphabet')
    @property
    def symbol_Q(self):
        return self.__symbol_Q
    @symbol_Q.setter
    def symbol_Q(self, value:set[State]):
            valid = True
            if(valid):
                self.__symbol_Q:set = value
            else:
                raise ValueError(f'Invalid set of states')
    @property
    def symbol_q_0(self):
            return self.__symbol_q_0  
    @symbol_q_0.setter
    def symbol_q_0(self, value:State):
            valid = True
            if(valid):
                self.__symbol_q_0 = value
            else:
                raise ValueError(f'Invalid start state')      
    @property
    def symbol_F(self):
            return self.__symbol_F
    @symbol_F.setter
    def symbol_F(self, value:set[State]):
            valid = True
            if(valid):
                self.__symbol_F = value
            else:
                raise ValueError(f'Invalid set of final states')
    
    
class NondeterministicFiniteAutomata(Automata):
    def __init__(self, symbol_Epsilon:set[str] = set(), symbol_Q:set[State] = set(), symbol_q_0:State = None, symbol_F: set[State] = set()):
        super().__init__(symbol_Epsilon, symbol_Q, symbol_q_0, symbol_F)
        pass

    @property
    def symbol_delta(self):
            return self.__symbol_delta
    
    @symbol_delta.setter
    def symbol_delta(self, value):
            valid = True
            if(valid):
                self.__symbol_delta = value
            else:
                raise ValueError(f'Invalid transition map')

    def transition_function(self):
        delta = []
        #Not implemented
        #for state in self.Q:
        #   for transition in state.transitions:
        #       delta.append((state.label, transition.target,transition.input))
        #
        delta = []
        delta.append(('q1','q1','0,1'))
        delta.append(('q1','q2','1'))
        delta.append(('q2','q3','0,1'))
        self.symbol_delta = delta
