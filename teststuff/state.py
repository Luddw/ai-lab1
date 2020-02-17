import datetime
import random
from locations import Locations
from message_types import MessageTypes
from telegram import Telegram

# base state class that all states inherit from
class State:
    def enter(self, entity):
        raise NotImplementedError

    def execute(self, entity, tick_size):
        raise NotImplementedError

    def exit(self, entity):
        raise NotImplementedError

    def on_message(self, entity, msg):
        raise NotImplementedError

# global state
class GlobalState(State):
    def enter(self, entity):
        return
    
    def execute(self, entity, tick_size):
        entity.increase_thirst(1*tick_size)
        entity.increase_hunger(1*tick_size)
        entity.increase_fatigue(1*tick_size)
        
        if entity.is_thirsty() and entity.current_state is not GoHomeAndSleep():
            entity.change_state(QuenchThirst())
        elif entity.is_hungry()and entity.current_state is not GoHomeAndSleep():
            entity.change_state(EatFood())
        
            
    def exit(self, entity):
        return
    def on_message(self, entity, msg):
        if msg.message_type is MessageTypes.SOCIAL_REQUEST and entity.is_hungry() is False:
            entity.change_state(Socialize())
            return True
        return False
    
    


# agent states
class Socialize(State):
    def enter(self, entity):
        if entity.location is not Locations.CAFE:
            print('[',str(entity.id),']: Walking to Cafe')
            entity.location = Locations.CAFE
        return

    def execute(self, entity, tick_size):
        entity.decrease_lonley(1*tick_size)
        print('[',str(entity.id),']: f i k a')   
        return

    def exit(self, entity):
        return

    def on_message(self, entity, msg):
        return
    
class Leisure(State):
    def enter(self, entity):
        print('[',str(entity.id),']: free time off work')

    def execute(self, entity, tick_size):
        
        pass
    
    def exit(self, entity):
        print('[',str(entity.id),']: back to being busy')
        
    def on_message(self, entity, msg):
        if msg.message_type is MessageTypes.SOCIAL_REQUEST and entity.is_hungry() is False:
            entity.change_state(Socialize())
            reply = Telegram(entity.id, msg.sender, MessageTypes.ACCEPT)
            entity.manager.dispatch_message(reply, 0)
            return True
        return False
        
    
class GoToWorkAndLabour(State):
    def enter(self, entity):
        work_msg_self = Telegram(entity.id, entity.id, MessageTypes.WORK_SELF)
        entity.manager.dispatch_message(work_msg_self, 8) #tick_size as msg delay
        if entity.location is not Locations.WORKPLACE:
            print('[',str(entity.id),']: Walking to work')
            entity.location = Locations.WORKPLACE

    def execute(self, entity, tick_size):
        print('[',str(entity.id),']: Earning money')
        entity.increase_money(1*tick_size)

    def exit(self, entity):
        if entity.is_rich():
            print('[',str(entity.id),']: Leaving Work! Did a good job today')

    def on_message(self, entity, msg):
        if msg.message_type is MessageTypes.WORK_SELF:
            entity.change_state(Shopping())
            return True
        return False
            
    
class GoToOfficeJob(State):
    def enter(self, entity):
        work_msg_self = Telegram(entity.id, entity.id, MessageTypes.WORK_SELF)
        entity.manager.dispatch_message(work_msg_self, 6) 
        if entity.location is not Locations.OFFICE:
            print('[',str(entity.id),']: Walking to the Office')
            entity.location = Locations.OFFICE

    def execute(self, entity, tick_size):
        entity.increase_money(2*tick_size)
        print('[',str(entity.id),']: pencil pusher getting money!')

        if entity.pockets_full():
            entity.change_state(QuenchThirst())

        if entity.is_thirsty():
            entity.change_state(QuenchThirst())

    def exit(self, entity):
        print('[',str(entity.id),']: Leaving OFFICE! Did a good job today')

    def on_message(self, entity, msg):
        return


class GoHomeAndSleep(State):
    def enter(self, entity):
        alarm_clock_msg = Telegram(entity.id, entity.id, MessageTypes.ALARM_CLOCK)
        entity.manager.dispatch_message(alarm_clock_msg, 8) #tick_size as msg delay
        if entity.location is not Locations.HOME:
            print('[',str(entity.id),']: Walking home to Sleep')
            entity.change_location(Locations.HOME)

    def execute(self, entity, tick_size):
            entity.decrease_fatigue(1*tick_size)
            print('[',str(entity.id),']: sleeping ZZZZ....')

    def exit(self, entity):
        print('[',str(entity.id),']: Leaving the house')

    #TODO messagesys for state
    def on_message(self, entity, msg):
        if msg.message_type is MessageTypes.ALARM_CLOCK:
            entity.change_state(GoToWorkAndLabour())
            return True
        return False


class Shopping(State):
    def enter(self, entity):
        print('[',str(entity.id),']: Spending my hard earned cash!')

    def execute(self, entity, tick_size):
        print('[',str(entity.id),']: Spending money in the shop')
        entity.spend_money()
        entity.change_state(GoHomeAndSleep())

    def exit(self, entity):
        print('[',str(entity.id),']: going back to whatever i was doing')

    def on_message(self, entity, msg):
        return
    
class QuenchThirst(State):
    def enter(self, entity):
        print('[',str(entity.id),']: Im thirsty!')
        #if entity.location is not Locations.TRAVVEN:
         #   print('[',str(entity.id),']: Im thirsty! Walking to Schtaans bästa student pub')
           # entity.change_location(Locations.TRAVVEN)

    def execute(self, entity, tick_size):
            entity.drink()
            print('[',str(entity.id),']: GLUGG GLUGG GLUGG!')
            entity.revert_to_previous_state()
    def exit(self, entity):
        print('[',str(entity.id),']: Thirst g o n e !')

    def on_message(self, entity, msg):
        return



class EatFood(State):

    def enter(self, entity):
        print('[',str(entity.id),']: Im very hungry')

    def execute(self, entity, tick_size):
        print('[',str(entity.id),']: NOM NOM NOM')
        entity.eat()
        entity.revert_to_previous_state()

    def exit(self, entity):
        print('[',str(entity.id),']: going back to whatever i was doing')

    def on_message(self, entity, msg):
        return 