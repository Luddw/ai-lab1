from enum import Enum


class MessageTypes(Enum):
    CAN_GO = 1
    CANT_GO = 2
    SOCIAL_REQUEST = 3
    WORK_SELF = 4
<<<<<<< HEAD
    ALARM_CLOCK = 5
    
=======
    ALARM_CLOCK = 5  

>>>>>>> 06d1d38630a20f6d9d0c42ae55deab776864ded0

def message_type_to_string(message_type):
    if message_type == MessageTypes.CAN_GO:
        return "I can go!"
    elif message_type == MessageTypes.CANT_GO:
        return "Sorry I can't go!"
    elif message_type == MessageTypes.SOCIAL_REQUEST:
        return "do you want to hang out?"
    else:
        return 'msgtype doesnt exist'
