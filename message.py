class Message:
    def __init__(self, sender, receiver, msgType, dispatchTime, info):
        self.sender = sender
        self.receiver = receiver
        self.msgType = msgType
        self.dispatchTime = dispatchTime
        self.info = info