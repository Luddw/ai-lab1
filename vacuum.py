from state import *
import time
from random import randint




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
        