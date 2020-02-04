
class BaseEntity:
    
    _nextValidID = 0
    
    def _SetID(self, value):
        assert value >= BaseEntity._nextValidID, "INVALID ID, YOURE BREAKING THE LAW"
        self.id = value
        BaseEntity._nextValidID = self.id + 1

    def __init__(self, ID, entitytype=-1):
        self._SetID(ID)
        self.currState = None
        self.prevState = None
        self.globalState = None

    def Update(self):
        pass
    
    def HandleMsg(self, msg):
        pass
    
    def BackToPrevState(self):
        pass