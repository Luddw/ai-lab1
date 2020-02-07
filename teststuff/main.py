from locations import Locations
from miner import Student
from state import StudentGlobalState, GoToWorkAndLabour
from wife import Wife
import time
class EntityManager:
    def __init__(self, tick_size):
        self.entities = {}
    
    def add_entity(self, entity):
        self.entities[entity.id] = entity
    
    def add_entity_dict(self, entities):
        for ent in entities:
            self.entities[ent.id] = ent
        
    def update(self, tick_size):
        for id in self.entities:
            self.entities[id].update(tick_size)

entmanager = EntityManager(1)
def main():
    miner = Student(1,current_state=GoToWorkAndLabour(), location=Locations.HOME, globalstate=StudentGlobalState())
    miner1 = Student(2,current_state=GoToWorkAndLabour(), location=Locations.HOME)
    entmanager.add_entity(miner)

    for i in range(100):
        entmanager.update(1)
if __name__ == '__main__':
    main()
