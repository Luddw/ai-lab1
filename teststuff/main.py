from locations import Locations
from agent import Agent
from state import *
from wife import Wife
import time
from entity_manager import EntityManager

entmanager = EntityManager(1)
def main():
    student = Agent(1,current_state=GoToWorkAndLabour(), location=Locations.HOME, globalstate=GlobalState())
    stud = Agent(2,current_state=GoHomeAndSleep(), location=Locations.HOME, globalstate=GlobalState())
    stud1 = Agent(3,current_state=Leisure(), location=Locations.HOME, globalstate=GlobalState())
    stud2 = Agent(4,current_state=Shopping(), location=Locations.HOME, globalstate=GlobalState())
    
    
    entmanager.add_entity(student)
    entmanager.add_entity(stud)
    entmanager.add_entity(stud1)
    entmanager.add_entity(stud2)
    for i in range(100):
        entmanager.update(1)
        
if __name__ == '__main__':
    main()

