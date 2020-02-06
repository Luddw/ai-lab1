from locations import Locations
from miner import Student
from state import *
from wife import Wife


def main():
    miner = Student(1,current_state=GoToWorkAndLabour(), location=Locations.HOME, globalstate=StudentGlobalState())
    miner1 = Student(2,current_state=GoToWorkAndLabour(), location=Locations.HOME)
    
    for i in range(0, 100):
        miner.update()


if __name__ == '__main__':
    main()
