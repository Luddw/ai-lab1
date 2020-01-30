from fsm import FSM
class BaseGameEntity:
    
    _nextValidID = 0
    
    def _SetID(self, value):
        assert value >= BaseGameEntity._nextValidID, "INVALID ID, YOURE BREAKING THE LAW"
        self._m_ID = value
        BaseGameEntity._nextValidID = self._m_ID + 1

    def __init__(self, ID):
        self._SetID(ID)

    def Update(self):
        pass

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
      #  self.FSM.AddState("Sleep", Sleep(self.FSM))
       # self.FSM.AddState("Eat",Eat(self.FSM))
        #self.FSM.AddState("Vacuum", Vacuum(self.FSM))

        
       # #ADD TRANSITIONS
       # self.FSM.AddTransition("toSleep", Transition("Sleep"))
        #self.FSM.AddTransition("toVacuum", Transition("Vacuum"))
        #self.FSM.AddTransition("toEat", Transition("Eat"))
                

    def Update(self):
        if self.FSM.currentState is not None:
            self.FSM.Execute()
        else:
            print("[miner.py]: STATE IS NONE, LAZY ASS")
    
    def Execute(self):
        self.FSM.Execute()