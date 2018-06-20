from multiprocessing import Pool

import numpy 
def sqr(x):
    return numpy.sqrt(x)
    
if __name__=='__main__':
    pool = Pool()
    roots = pool.map(sqr,range(100))
    print(roots)