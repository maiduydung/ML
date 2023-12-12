import multiprocessing
import time
def print_1():
    while True:
        print (1)
        time.sleep(2)

def print_2():
     while True:
        print(2)
        time.sleep(2)
if __name__ == '__main__':
    p1 = multiprocessing.Process(name='p1', target=print_1)
    p2 = multiprocessing.Process(name='p2', target=print_2)
    p1.start()
    p2.start()