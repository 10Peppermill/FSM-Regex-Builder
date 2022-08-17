from encodings import utf_8
from typing import List
from greenery import fsm, lego
import FSMState
import FSMTransition

class FSMStateMachine:
    
    StatesList:     list

    __FSM_Q:        set
    __FSM_Sigma:    set
    __FSM_q0:       int
    __FSM_F:        set
    __FSM_delta:    dict

    def __init__(self) -> None:
        pass

    def Set_SetOfStates(self, fsm_Q: list[FSMState.FSMState]):
        self.fsm_Q = set(x.SelfStateIdentifier for x in fsm_Q)

    def Set_Alphabet(self, fsm_Sigma: set):
        self.FSM_Sigma = fsm_Sigma

    def Set_InitalState(self, fsm_Q: list[FSMState.FSMState]):
        self.FSM_F
    
    def Set_SetofAcceptStates(self, fsm_Q: list[FSMState.FSMState]):
        self.FSM_F = set(x.SelfStateIdentifier for x in fsm_Q if x.FinalState == True)


# create the FSM
finiteAutomata = fsm.fsm(
    states      = fsm_Q,
    alphabet    = fsm_Sigma,
    initial     = fsm_q0,
    finals      = fsm_F,
    map         = fsm_delta 
)
print(finiteAutomata)