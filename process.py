import sys
from typing import Dict
from greenery import fsm, lego

UC = set(hex(e) for e in range(sys.maxunicode))
UC_NUMBERS = set(chr(e) for e in range(48,57,1))
UC_UPPERS = set(chr(e) for e in range(65,90,1))
UC_LOWERS = set(chr(e) for e in range(97,122,1))
#UC = set(range(sys.maxunicode))
#UC_NUMBERS = set(range(48,57,1))
#UC_UPPERS = set(range(65,90,1))
#UC_LOWERS = set(range(97,122,1))
EMPTY_SET = set()


Q1, Q2 = range(2)

a_Q = {Q1,Q2}
a_Sigma = EMPTY_SET.union(UC_NUMBERS, UC_LOWERS, UC_UPPERS)
a_q = Q1
a_F = {Q2}

finiteAutomata = fsm.fsm(
    states      = a_Q,
    alphabet    = a_Sigma,
    initial     = a_q,
    finals      = a_F,
    map         = {
         Q1 : {str(UC_NUMBERS): Q2, str(UC_LOWERS): Q1, str(UC_UPPERS): Q1},
         Q2 : {str(UC_NUMBERS): Q2, str(UC_LOWERS): Q2, str(UC_UPPERS): Q2}
    } 
)
# create the FSM


# convert it to regex
rex = lego.from_fsm(finiteAutomata)
print(rex)