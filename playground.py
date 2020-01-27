from random import randint
from time import clock


class FSM:
    def __init__(self, agent):
        self.agent = agent
        self.states = {}
        self.transitions = {}
        self.currentState = None
        self.previousState = None
        self.transition = None
    
    def AddTransition(self, transitionName, transition):
        self.transition[transitionName] = transition
    
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



class Transition:
    def __init__(self, toState):
        self.toState = toState
        
    def Execute(self):
        print("Transitioning...")
        

class State:
    def __init__(self, FSM):
        self.FSM = FSM
        self.timer = 0
        self.startTime = 0
        
    def Enter(self):
        self.timer = randint(0, 5)
        self.startTime = int(clock())
    
    def Execute(self):
        pass
    
    def Exit(self):
        pass

class CleanDishes(State):
    def __init__(self, FSM):
        super(CleanDishes, self).__init__(FSM)
    
    def Enter(self):
        print("Cleaning Dishes")
        super(CleanDishes, self).Enter()
        
    def Execute(self):
        print("cleaning dishes")
        
        if(self.startTime + self.timer <= clock()):
            if not (randint(1, 3) % 2):
                self.FSM.ToTransition("toVacuum")
            else:
                self.FSM.ToTransition("toSleep")
                