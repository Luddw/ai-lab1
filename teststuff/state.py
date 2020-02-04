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


# Miner states
class GoToWorkAndLabour(State):
    def enter(self, entity):
        if entity.location is not Locations.WORKPLACE:
            print("Walking to work")
            entity.location = Locations.WORKPLACE

    def execute(self, entity):
        # Getting dosh!
        entity.increase_money(1)

        # Diggy diggy hål
        entity.increase_fatigue()

        print(str(entity.id),'Earning money')

        if entity.pockets_full():
            entity.change_state(QuenchThirst())

        if entity.is_thirsty():
            entity.change_state(QuenchThirst())

    def exit(self, entity):
        print(str(entity.id),'Leaving Work! Did a good job today')

    def on_message(self, entity, msg):
        return


class GoHomeAndSleep(State):
    def enter(self, entity):
        if entity.location is not Locations.HOME:
            print('Walking home')
            entity.change_location(Locations.HOME)

    def execute(self, entity):
        if entity is not entity.is_fatigue():
            print(str(entity.id),'I slept like a log!!')
            entity.change_state(GoToWorkAndLabour())
        else:
            entity.descrease_fatigue()
            print(str(entity.id),'ZZZZ....')

    def exit(self, entity):
        print('Leaving the house')

    def on_message(self, entity, msg):
        if msg.message_type == MessageTypes.STEW_READY:
            print('Message handled by {} at time: {}'.format(str(entity.id), datetime.datetime.now()))
            entity.change_state(EatFood())

class Shopping(State):
    def enter(self, entity):
        print(str(entity.id),'Spending my hard earned cash!')

    def execute(self, entity):
        print(str(entity.id),'Spending money in the shop')
        entity.spend_money()
        entity.revert_to_previous_state()

    def exit(self, entity):
        print(str(entity.id),'going back to whatever i was doing')

    def on_message(self, entity, msg):
        return
    
class QuenchThirst(State):
    def enter(self, entity):
        if entity.location is not Locations.TRAVVEN:
            print('[',str(entity.id),']: "Im thirsty! Walking to Schtaans bästa student pub"')
            entity.change_location(Locations.TRAVVEN)

    def execute(self, entity):
        if entity.is_thirsty():
            entity.drink()
            print('[',str(entity.id),']: Thirst gone!')
            entity.change_state(GoToWorkAndLabour())

    def exit(self, entity):
        print('Leaving travven!')

    def on_message(self, entity, msg):
        return



class EatFood(State):

    def enter(self, entity):
        print(str(entity.id),'Im very hungry')

    def execute(self, entity):
        print(str(entity.id),'NOM NOM NOM')
        entity.eat()
        entity.revert_to_previous_state()

    def exit(self, entity):
        print(str(entity.id),'going back to whatever i was doing')

    def on_message(self, entity, msg):
        return