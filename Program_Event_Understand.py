import time
import threading
from random import randint

# wydarzeniami mozna sterowac za pomoca Event()
# set ustawia na True
# clear ustawia na False
# jak wywolamy wait to czeka az dostanie set i zrobi cos dalej


def flag():
    time.sleep(3)
    Taki_sterownik_thareadami.set()
    print("start_counting, i teraz przez 7 sekund bedzie sie wykonywac start_operations")
    time.sleep(10)
    print("event is cleared")
    Taki_sterownik_thareadami.clear()
def start_operations():
    Taki_sterownik_thareadami.wait()
    while Taki_sterownik_thareadami.is_set():
        print("starting random integer task")
        x = randint(1,100)
        print("x = ",x)
        time.sleep(1)
    print("Zakonczony start_operations")

Taki_sterownik_thareadami = threading.Event()
t1 = threading.Thread(target = flag)
t2 = threading.Thread(target = start_operations)

t1.start()
t2.start()

