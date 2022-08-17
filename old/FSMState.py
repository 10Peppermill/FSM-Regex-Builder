from FSMTransition import FSMTransition
__SIGMA__ = set(chr(e) for e in range(48,(2**7)-1,1))

class FSMState:
    SelfStateIdentifier: int
    FinalState: bool
    InitalState: bool
    __StateTransitionsDict: dict
    __StateTransitionsList: list
    __AllTransitionChars: set
    
    def __init__(self, selfStateIdentifier: int, finalState: bool, initalstate: bool) -> None:
        self.SelfStateIdentifier = selfStateIdentifier
        self.FinalState = finalState
        self.InitalState = initalstate

    def AddTransition(self, transitionInvokingChars: set, targetStateIdentifier: int):
        self.__StateTransitionsDict.update(transitionInvokingChars, targetStateIdentifier)
        newTransition = FSMTransition(transitionInvokingChars, targetStateIdentifier)
        self.__StateTransitionsList.append(newTransition)
        self.__AllTransitionChars = self.__AllTransitionChars.union(transitionInvokingChars)

    def RemoveTransition(self, transitionToRemove: FSMTransition):
        #update the chars that are purposefully used by this state
        self.__AllTransitionChars = self.__AllTransitionChars.difference(transitionToRemove.TransitionInvokingChars)
        #remove the transiton from the transitions list
        self.__StateTransitionsList.remove(transitionToRemove)
        #update the stateTransitions dictionary to have all now unused chars loop on self
        self.__StateTransitionsDict.update(__SIGMA__.difference(self.__AllTransitionChars), self.SelfStateIdentifier)

    def GetDictionary(self) -> dict:
        return self.__StateTransitionsDict