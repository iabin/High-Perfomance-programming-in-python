import sys, threading, multiprocessing, time

def countdown(n):
    while n > 0:
        n-=1
        
COUNT = 100000000
t = time.time()
    
if sys.argv[1]=='serial':
    countdown(COUNT)
    print("SERIAL Me tomo: "+str(time.time()-t))
    
if sys.argv[1]=='parallel':
    countdown(COUNT)
    t1 = threading.Thread(target=countdown,args=(COUNT//2,))
    t2 = threading.Thread(target=countdown,args=(COUNT//2,))
    t1.start();t2.start()
    t1.join();t2.join();  
    print("PARALLEL Me tomo: "+str(time.time()-t))
    
if sys.argv[1]=='process':
    countdown(COUNT)
    t1 = multiprocessing.Process(target=countdown,args=(COUNT//2,))
    t2 = multiprocessing.Process(target=countdown,args=(COUNT//2,))
    t1.start();t2.start()
    t1.join();t2.join();
    print("PROCESS Me tomo: "+str(time.time()-t))
    