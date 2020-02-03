from state import Eat, Vacuum, Sleep
from fsm import FSM
from transition import Transition



Character = type("Char",(object,),{})



class Student(Character):
    def __init__(self):
        self.FSM = FSM(self)
        
        
        #ADD STATES
        self.FSM.AddState("Sleep", Sleep(self.FSM))
        self.FSM.AddState("Eat",Eat(self.FSM))
        self.FSM.AddState("Vacuum", Vacuum(self.FSM))

        
        #ADD TRANSITIONS
        self.FSM.AddTransition("toSleep", Transition("Sleep"))
        self.FSM.AddTransition("toVacuum", Transition("Vacuum"))
        self.FSM.AddTransition("toEat", Transition("Eat"))
        
        
        self.FSM.SetState("Sleep")
    
    def Execute(self):
        self.FSM.Execute()