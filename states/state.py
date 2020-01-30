import time
from random import randint


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