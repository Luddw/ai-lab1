class BaseGameEntity:


    def _SetID(self, value):
        self._m_ID = value

    def __init__(self, ID):
        self._m_ID          = ID
        self._m_NextValidID = 0

    def Update(self):
        pass


class Miner(BaseGameEntity):
    def __init__(self, ID):
        self.m_currentState  = State()
        self.m_location      = Location("kek")
        self.m_currentGold   = 0
        self.m_goldInBank    = 0
        self.m_thirst        = 0
        self.m_fatigue       = 0
    
    def Update(self):
        self.m_thirst += 1
        if self.m_currentState in locals():
            print(self.m_currentState)
            self.m_currentState
        
    
    def ChangeState(self, newState):
        self.m_currentState.Exit(self)
        self.m_currentState = newState
        self.m_currentState.Enter(self)
        pass

class State(object):
    def Enter(self, actor):
        pass
    def Execute(self, actor):
        pass
    def Exit(self, actor):
        pass

class Location:
    def __init__(self, name):
        self.m_name = name

class SingletonDecor:
    def __init__(self,klass):
        self.klass = klass
        self.instance = None
    def __call__(self,*args,**kwds):
        if self.instance == None:
            self.instance = self.klass(*args,**kwds)
        return self.instance

class EnterMineAndDigForGold(SingletonDecor, State):
    def Enter(self):
        pass
    
    Execute


