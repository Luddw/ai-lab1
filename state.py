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
        if():
            if not (randint(1, 3) % 2):
                self.FSM.ToTransition("toVacuum")
            else:
                self.FSM.ToTransition("toEat")
    
    def Exit(self):
        print("WAKING UPPP (grab a brush and put on a little make up)")
    
