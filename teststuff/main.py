from locations import Locations
from agent import Agent
from state import GlobalState, GoToWorkAndLabour, Shopping
from wife import Wife
import time
from entity_manager import EntityManager

entmanager = EntityManager(1)
def main():
    student = Agent(1,current_state=GoToWorkAndLabour(), location=Locations.HOME, globalstate=GlobalState())
    stud = Agent(2,current_state=GoToWorkAndLabour(), location=Locations.HOME)
    entmanager.add_entity(student)

    for i in range(100):
        entmanager.update(1)
        
if __name__ == '__main__':
    main()
