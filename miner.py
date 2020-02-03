from fsm import FSM
from basegameentity import BaseGameEntity
from eat import Eat
from vacuum import Vacuum
from sleep import Sleep
from transition import Transition


print(BaseGameEntity._nextValidID)
BaseGameEntity(0)
print(BaseGameEntity._nextValidID)
BaseGameEntity(1)
print(BaseGameEntity._nextValidID)


class Student(BaseGameEntity):
    def __init__(self, ID):
        self.FSM = FSM(self)
        self.thirst = 0
        self.money = 0
        self.fatigue = 0
    
        
        #ADD STATES
        self.FSM.AddState("Sleep", Sleep(self.FSM))
        self.FSM.AddState("Eat",Eat(self.FSM))
        self.FSM.AddState("Vacuum", Vacuum(self.FSM))

        
        #ADD TRANSITIONS
        self.FSM.AddTransition("toSleep", Transition("Sleep"))
        self.FSM.AddTransition("toVacuum", Transition("Vacuum"))
        self.FSM.AddTransition("toEat", Transition("Eat"))
                

    def Update(self):
        if self.FSM.currentState is not None:
            self.thirst += 1
            self.FSM.Execute()
        else:
            print("[miner.py]: STATE IS NONE, LAZY ASS")
    
    def Execute(self):
        self.FSM.Execute()