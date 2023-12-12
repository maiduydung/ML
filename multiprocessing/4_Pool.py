def f1(args):
    a, b, c = args[0] , args[1] , args[2]
    return a+b+c

if __name__ == "__main__":
    import multiprocessing
    pool = multiprocessing.Pool(4) 

    result1 = pool.map(f1, [ [1,2,3] ])
    print(result1)