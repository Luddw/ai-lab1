import time
from state import *
from random import randint


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