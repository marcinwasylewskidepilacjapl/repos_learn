import time
import multiprocessing
square_result = []
def calc_square(numbers):
    global square_result
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square:", n**2)
        square_result.append(n**2)
def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cube:", n**3)

arr = [2,3,8,9]

t = time.time()
p1 = multiprocessing.Process(target=calc_square, args=(arr,))
p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
p1.start()
p2.start()
p1.join()
p2.join()
print("done in: ", time.time()-t)
print("Done work", square_result)
#Nie wydrukowal nic w square_result bo w multiprocessingu kazdy nowy process tworzy kopie zmiennych majacych wlasny adress_space (virtual memory)
#Sa one rozne dla procesu glownego i procesow swtorzonych przez uzytkownika
#jesli bysmy chcieli skorelowac dane square_result potrzeba wtedy IPC (interprocess) technik