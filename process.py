from inspect import Attribute
import sys
from typing import Dict
from greenery import fsm, lego
import re
import numpy

UC = set(chr(e) for e in range(48,(2**7)-1,1))
UC_NUMBERS = set(chr(e) for e in range(48,58,1))
UC_UPPERS = set(chr(e) for e in range(65,91,1))
UC_LOWERS = set(chr(e) for e in range(97,123,1))
EMPTY_SET = set()

transitionFunction = dict()
state1 = dict()
state2 = dict()
Q1, Q2 = range(2)
localLanguage = EMPTY_SET.union(UC_NUMBERS, UC_LOWERS, UC_UPPERS)

a_Q = {Q1,Q2}
a_Sigma = UC
a_q = Q1
a_F = {Q1}

diffrence = a_Sigma.difference(localLanguage)

for e in UC_NUMBERS:
    state1.update({e : Q2})
for e in UC_UPPERS:
    state1.update({e : Q1})
for e in UC_LOWERS:
    state1.update({e : Q1})
for e in diffrence:
    state1.update({e : Q2})

for e in UC_NUMBERS:
    state2.update({e : Q2})
for e in UC_UPPERS:
    state2.update({e : Q2})
for e in UC_LOWERS:
    state2.update({e : Q2})
for e in diffrence:
    state2.update({e : Q2})

transitionFunction.update({Q1 : state1})
transitionFunction.update({Q2 : state2})

# create the FSM
finiteAutomata = fsm.fsm(
    states      = a_Q,
    alphabet    = a_Sigma,
    initial     = a_q,
    finals      = a_F,
    map         = transitionFunction 
)
print(finiteAutomata)

# convert it to regex
rex = lego.from_fsm(finiteAutomata)
print(rex)

print("BYE")