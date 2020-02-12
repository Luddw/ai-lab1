
class BaseEntity:
    
    _nextValidID = 0
    
    def _setID(self, value):
        assert value >= BaseEntity._nextValidID, "INVALID ID, YOURE BREAKING THE LAW"
        self.id = value
        BaseEntity._nextValidID = self.id + 1

    def __init__(self, ID, entitytype=-1):
        self._setID(ID)
        self.currState = None
        self.prevState = None
        self.globalState = None
        self.manager = None
        
    def update(self):
        pass
    
    def handleMsg(self, msg):
        pass
    
    def backToPrevState(self):
        pass