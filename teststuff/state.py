import datetime
import random
from locations import Locations
from message_dispatcher import MessageDispatcher
from message_types import MessageTypes


class State:
    def enter(self, entity):
        raise NotImplementedError

    def execute(self, entity):
        raise NotImplementedError

    def exit(self, entity):
        raise NotImplementedError

    def on_message(self, entity, msg):
        raise NotImplementedError

class StudentGlobalState(State):
    def enter(self, entity):
        return
    
    def execute(self, entity):
        entity.increase_thirst()
        entity.increase_hunger()
        
        if entity.fatigue <= 0:
            if entity.thirst > 10 and entity.current_state is not QuenchThirst():
                entity.change_state(QuenchThirst())
                pass
            pass
        
        if entity.money == entity.MAX_MONEY:
            entity.change_state(Shopping())
        
        if entity.fatigue >= 50:
            entity.change_state(GoHomeAndSleep())
    
    def exit(self, entity):
        return
    def on_message(self, msg):
        if msg.message_type :
            pass
        
        
# agent states
class GoToWorkAndLabour(State):
    def enter(self, entity):
        if entity.location is not Locations.WORKPLACE:
            print('[',str(entity.id),']: Walking to work')
            entity.location = Locations.WORKPLACE

    def execute(self, entity):
        print('[',str(entity.id),']: Earning money')
        entity.increase_fatigue(1)
        entity.increase_money(1)

        if entity.money == entity.MAX_MONEY:
            entity.change_state(QuenchThirst())

        if entity.is_thirsty():
            entity.change_state(QuenchThirst())

    def exit(self, entity):
        print('[',str(entity.id),']: Leaving Work! Did a good job today')

    def on_message(self, entity, msg):
        return
    
class GoToOfficeJob(State):
    def enter(self, entity):
        if entity.location is not Locations.OFFICE:
            print('[',str(entity.id),']: Walking to the Office')
            entity.location = Locations.OFFICE

    def execute(self, entity):
        # Getting dosh!
        entity.increase_money(2)

        # Diggy diggy hål
        entity.increase_fatigue(2)

        print('[',str(entity.id),']: Tiring office job, keep Earning money!')

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
        if entity.location is not Locations.HOME:
            print('[',str(entity.id),']: Walking home to Sleep')
            entity.change_location(Locations.HOME)

    def execute(self, entity):
        if entity is not entity.is_fatigue():
            print('[',str(entity.id),']: I slept pretty well')
            entity.change_state(GoToWorkAndLabour())
        else:
            entity.descrease_fatigue()
            print('[',str(entity.id),']: ZZZZ....')

    def exit(self, entity):
        print('[',str(entity.id),']: Leaving the house')

    #TODO messagesys for state
    def on_message(self, entity, msg):
        if msg.message_type:
            print('Message handled by {} at time: {}'.format(str(entity.id), datetime.datetime.now()))
            entity.change_state(EatFood())

class Shopping(State):
    def enter(self, entity):
        print('[',str(entity.id),'Spending my hard earned cash!')

    def execute(self, entity):
        print('[',str(entity.id),'Spending money in the shop')
        entity.spend_money()
        entity.revert_to_previous_state()

    def exit(self, entity):
        print('[',str(entity.id),'going back to whatever i was doing')

    def on_message(self, entity, msg):
        return
    
class QuenchThirst(State):
    def enter(self, entity):
        print('[',str(entity.id),']: Im thirsty!')
        #if entity.location is not Locations.TRAVVEN:
         #   print('[',str(entity.id),']: Im thirsty! Walking to Schtaans bästa student pub')
           # entity.change_location(Locations.TRAVVEN)

    def execute(self, entity):
        if entity.is_thirsty():
            entity.drink()
            print('[',str(entity.id),']: GLUGG GLUGG GLUGG!')
            entity.revert_to_previous_state()

    def exit(self, entity):
        print('[',str(entity.id),']: Thirst g o n e !')

    def on_message(self, entity, msg):
        return



class EatFood(State):

    def enter(self, entity):
        print('[',str(entity.id),'Im very hungry')

    def execute(self, entity):
        print('[',str(entity.id),'NOM NOM NOM')
        entity.eat()
        entity.revert_to_previous_state()

    def exit(self, entity):
        print('[',str(entity.id),'going back to whatever i was doing')

    def on_message(self, entity, msg):
        return