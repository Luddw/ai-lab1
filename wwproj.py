from random import randint
import time


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
        self.startTime = int(time.process_time())
    
    def Execute(self):
        pass
    
    def Exit(self):
        pass

class Eat(State):
    def __init__(self, FSM):
        super(Eat, self).__init__(FSM)
    
    def Enter(self):
       
        super(Eat, self).Enter()
        
    def Execute(self):
        print("Eat")
        
        if(self.startTime + self.timer <= time.process_time()):
            if not (randint(1, 3) % 2):
                self.FSM.ToTransition("toVacuum")
            else:
                self.FSM.ToTransition("toSleep")
    
    def Exit(self):
        print("Finished Eat")


class Vacuum(State):
    def __init__(self, FSM):
        super(Vacuum, self).__init__(FSM)
    
    def Enter(self):
        print("Start Vacuum cleaner")
        super(Vacuum, self).Enter()
        
    def Execute(self):
        print("VACOOOOOOOOOOOOMING")
        if(self.startTime + self.timer <= time.process_time()):
            if not (randint(1, 3) % 2):
                self.FSM.ToTransition("toSleep")
            else:
                self.FSM.ToTransition("toEat")
    
    def Exit(self):
        print("Finished Vacuum")
        
class Sleep(State):
    
    def __init__(self, FSM):
        super(Sleep, self).__init__(FSM)
        self.sleepAmount = 0
        self.startTime = 0
    
    def Enter(self):
        print("starting to SLEEP")
        super(Sleep, self).Enter()
    
    def Execute(self):
        print("SLEEPING")
        if(self.startTime + self.timer <= time.process_time()):
            if not (randint(1, 3) % 2):
                self.FSM.ToTransition("toVacuum")
            else:
                self.FSM.ToTransition("toEat")
    
    def Exit(self):
        print("WAKING UPPP (grab a brush and put on a little make up)")
    


Character = type("Char",(object,),{})

class Student(Character):
    def __init__(self):
        self.FSM = FSM(self)
        
        
        self.FSM.AddState("Sleep", Sleep(self.FSM))
        self.FSM.AddState("Eat",Eat(self.FSM))
        self.FSM.AddState("Vacuum", Vacuum(self.FSM))

        self.FSM.AddTransition("toSleep", Transition("Sleep"))
        self.FSM.AddTransition("toVacuum", Transition("Vacuum"))
        self.FSM.AddTransition("toEat", Transition("Eat"))
        
        
        self.FSM.SetState("Sleep")
    
    def Execute(self):
        self.FSM.Execute()



student = Student()
for i in range(20):
    startTime = time.process_time()
    timeInterval = 1
    while(startTime + timeInterval > time.process_time()):
        pass
    print("[Current time]: ", i, "s \n")
    student.FSM.Execute()
    print("-----------------------------")