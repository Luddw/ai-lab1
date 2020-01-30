class FSM:
    def __init__(self, agent):
        self.agent = agent
        self.states = {}
        self.transitions = {}
        self.currentState = None
        self.previousState = None
        self.transition = None
    
    def AddTransition(self, transitionName, transition):
        self.transitions[transitionName] = transition
    
    def AddState(self, stateName, state):
        self.states[stateName] = state
        
    def SetState(self, stateName):
        self.previousState = self.currentState
        self.currentState = self.states[stateName]

    def ToTransition(self,toTransition):
        self.transition = self.transitions[toTransition]
    
    def Execute(self):
        if self.transition:
            self.currentState.Exit()
            self.transition.Execute()
            self.SetState(self.transition.toState)
            self.currentState.Enter()
            self.transition = None
        self.currentState.Execute()