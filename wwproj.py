from random import randint
import time
from student import Student


STARTTIME = time.monotonic()
student = Student()
if __name__ == "__main__":
    for i in range(20):
        startTime = time.process_time()
        timeInterval = 1
        while(startTime + timeInterval > time.process_time()):
            pass
        print("[Current time]: ", i, "s")
        student.FSM.Execute()
        print("-----------------------------")
