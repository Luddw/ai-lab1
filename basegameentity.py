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