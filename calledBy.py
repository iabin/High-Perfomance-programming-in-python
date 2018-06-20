import threading
def function(i):
    print("Function called by: "+str(i))
    return

pool = []
for i in range(5):
    t = threading.Thread(target=function,args=(i,))
    pool.append(t)
   
for t in pool:
    t.start()
    t.join()
