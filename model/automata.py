from abc import abstractmethod
from state import State
from transition import Transition

class Automata:
    def __init__(self, Epsilon:set[str], Q:set[State], q_0:State, F:set[State]) -> None:
        self.Epsilon = Epsilon
        self.Q = Q
        self.q_0 = q_0
        self.F = F

        @property
        def Epsilon(self):
            return self.__Epsilon
        
        @Epsilon.setter
        def Epsilon(self, value:set[str]):
            valid = True
            if(valid):
                self.__Epsilon = value
            else:
                raise ValueError(f'Invalid Alphabet')
        
        @property
        def Q(self):
            return self.__Q
        
        @Q.setter
        def Q(self, value:set[State]):
            valid = True
            if(valid):
                self.__Q = value
            else:
                raise ValueError(f'Invalid set of states')

        @property
        def q_0(self):
            return self.__q_0
        
        @q_0.setter
        def q_0(self, value:State):
            valid = True
            if(valid):
                self.__q_0 = value
            else:
                raise ValueError(f'Invalid start state')
            
        @property
        def F(self):
            return self.__F
        
        @F.setter
        def F(self, value:set[State]):
            valid = True
            if(valid):
                self.__F = value
            else:
                raise ValueError(f'Invalid set of final states')

        @abstractmethod
        def __transition_function__(self):
            pass

class NondeterministicFiniteAutomata(Automata):
    def __init__(self, Epsilon:set[str] = {}, Q:set[State] = {}, q_0:State = None, F: set[State] = {}):
        super().__init__(Epsilon, Q, q_0, F)
        pass

        @property
        def delta(self):
            return self.__delta
        
        @delta.setter
        def delta(self, value):
            valid = True
            if(valid):
                self.__delta = value
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
        self.delta = delta
