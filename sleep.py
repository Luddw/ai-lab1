from state import *
import time
from random import randint


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
    
