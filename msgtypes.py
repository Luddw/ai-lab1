from enum import Enum

class MessageType(Enum):
    CAN_GO = 0
    CANT_GO = 1


def msgTypeToStr(msgType):
    if msgType == MessageType.CAN_GO:
        return "I can go!"
    elif msgType == MessageType.CANT_GO:
        return "Sorry I can't go!"
    else:
        return 'msgtype doesnt exist'