from beepy import beep
from time import sleep

PO = 0 # Progressive Overload time
PO_REP = 0 # Progressive Overload reps
REP = 7 # 7 seconds for 1 rep 
beep(4)
def work(time,name):
    sleep(time+PO)
    beep(4)
    beep(4)
    beep(4)
    print(name + " : " + time + " s")
def rest(time):
    sleep(time)
    beep(4)
    beep(4)
    beep(4)
    print("Rest : " + time + " s")
#Dead Hangs
work(60,"Hang")
rest(300) # 5min
work(50,"Hang")
rest(300) # 5min
work(40,"Hang")
rest(300) # 5min

#Pull Ups
work((5+PO_REP)*REP,"Pull Up")
rest(180) # 3min
work((3+PO_REP)*REP,"Pull Up")
rest(180) # 3min
work((1+PO_REP)*REP,"Pull Up")
rest(180) # 3min

