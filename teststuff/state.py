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

    def on_message(self, entity, telegram):
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
            entity.change_state()

        if entity.is_thirsty():
            entity.change_state(QuenchThirst())

    def exit(self, entity):
        print(str(str(entity.id)),'Leaving Work! Did a good job today')

    def on_message(self, entity, telegram):
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

    def on_message(self, entity, telegram):
        if telegram.message_type == MessageTypes.STEW_READY:
            print('Message handled by {} at time: {}'.format(str(entity.id), datetime.datetime.now()))
            print('Okay hun, ahm a coming')
            entity.change_state(EatStew())


class QuenchThirst(State):
    def enter(self, entity):
        if entity.location is not Locations.TRAVVEN:
            print('[',str(entity.id),']: Im thirsty! Walking to Schtaans bästa student pub')
            entity.change_location(Locations.TRAVVEN)

    def execute(self, entity):
        if entity.is_thirsty():
            entity.drink()
            print('[',str(entity.id),']: Thirst gone!')
            entity.change_state(GoToWorkAndLabour())

    def exit(self, entity):
        print('Leaving the saloon, feeling good')

    def on_message(self, entity, telegram):
        return



class EatStew(State):

    def enter(self, entity):
        print('Smells really good Elsa')

    def execute(self, entity):
        print('Tastes really good too')
        entity.revert_to_previous_state()

    def exit(self, entity):
        print('Thank ya little lady. Ah better get back to whatever ah wuz doing')

    def on_message(self, entity, telegram):
        return


# Wife states
class WifeGlobalState(State):
    def enter(self, entity):
        return

    def execute(self, entity):
        if random.randint(0, 10) == 3 and entity.current_state is not VisitTheBathroom():
            entity.change_state(VisitTheBathroom())

    def exit(self, entity):
        return

    def on_message(self, entity, telegram):
        if telegram.message_type == MessageTypes.HI_HONEY_I_AM_HOME:
            print('Message received by {} at time: {}'.format(str(entity.id), datetime.datetime.now()))
            print('Hi Honey. Let me make you some of mah fine country stew')
            entity.change_state(CookStew())


class DoHouseWork(State):
    def enter(self, entity):
        print('Time to do some housework')

    def execute(self, entity):

        if not entity.is_stressed():
            case = random.randint(0, 2)
            if case == 0:
                print('Mopping the flor')
                return

            if case == 1:
                print('Washing the dishes')
                return

            if case == 2:
                print('Making the bed')
                return
        else:
            entity.change_state(VisitTheBathroom())

    def exit(self, entity):
        return

    def on_message(self, entity, telegram):
        return


class VisitTheBathroom(State):
    def enter(self, entity):
        print('Walking to the can. Need to powda my pretty little nose')

    def execute(self, entity):
        print('Ahhhhhh! sweet relief')
        entity.change_state(DoHouseWork())

    def exit(self, entity):
        print('Leaving the Jon')

    def on_message(self, entity, telegram):
        return


class CookStew(State):
    def enter(self, entity):
        if not entity.is_cooking:
            print('Putting the stew in the oven')
            entity.set_is_cooking(True)

    def execute(self, entity):
        print('Fussing over the food')

    def exit(self, entity):
        print('Putting the stew on the table')

    def on_message(self, entity, telegram):
        if telegram.message_type == MessageTypes.HI_HONEY_I_AM_HOME:
            print('Message received by {} at time: {}'.format(str(entity.id), datetime.datetime.now()))
            print('Stew is Ready! Lets eat')

            message_dispatcher = MessageDispatcher()
            message_dispatcher.dispatch_message(0, entity, entity.other_entity, MessageTypes.STEW_READY, '')

            entity.is_cooking = False
            entity.change_state(DoHouseWork())
