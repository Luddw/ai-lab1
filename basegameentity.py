from message import Message

class BaseGameEntity:
    
    _nextValidID = 0
    
    def _SetID(self, value):
        assert value >= BaseGameEntity._nextValidID, "INVALID ID, YOURE BREAKING THE LAW"
        self._m_ID = value
        BaseGameEntity._nextValidID = self._m_ID + 1

    def __init__(self, ID=1):
        self._SetID(ID)
        self.currState = None
        self.prevState = None
        self.globalState = None

    def update(self):
        pass
    
    def handleMsg(self, msg):
        pass
    
    def backToPrevState(self):
        pass