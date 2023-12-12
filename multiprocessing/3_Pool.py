from multiprocessing import Pool
import time

work = (["A", 4], ["B", 1], ["C", 3], ["D", 3])

def work_log(work_data):
    print('Process {0} is waiting {1} seconds'.format(work_data[0], work_data[1]))
    time.sleep(work_data[1])
    print('Process {0} is done'.format(work_data))

def pool_handler():
    p = Pool(2)
    p.map(work_log, work)

if __name__ == '__main__':
    pool_handler()