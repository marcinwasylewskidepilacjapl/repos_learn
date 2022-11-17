import time
import threading
def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square:", n**2)
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube:", n**3)

arr = [2,3,8,9]

t = time.time()
wątekp1 = threading.Thread(target=calc_square, args=(arr,))
wątekp2 = threading.Thread(target=calc_cube, args=(arr,))
wątekp1.start()
wątekp2.start()
wątekp1.join()
wątekp2.join()
print("done in: ", time.time()-t)
print("Done work")