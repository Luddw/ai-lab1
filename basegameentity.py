

class BaseGameEntity:
    nextValidID = 0
    def __init__(self, ID):
        self.SetID(ID)
    
    def SetID(self, value):
        self.ID = value
        nextValidID =  self.ID + 1