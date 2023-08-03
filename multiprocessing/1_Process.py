from multiprocessing import Process

def print_func(continent='Asia'):
    res = 'The name of continent is : {}'.format(continent)
    print(res)
    return res

if __name__ == '__main__':
    names = ['America', 'Europe', 'Africa']
    procs = []
    for name in names:
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()