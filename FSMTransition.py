class FSMTransition:
    TargetStateIdentifier: int
    TransitionInvokingChars: set
    def __init__(self, transitionInvokingChars, targetStateIdentifier) -> None:
        self.TargetStateIdentifier = targetStateIdentifier
        self.TransitionInvokingChars = transitionInvokingChars