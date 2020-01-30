from random import randint
import time
from student import *



student = Student()
for i in range(20):
    startTime = time.process_time()
    timeInterval = 1
    while(startTime + timeInterval > time.process_time()):
        pass
    print("[Current time]: ", i, "s \n")
    student.FSM.Execute()
    print("-----------------------------")