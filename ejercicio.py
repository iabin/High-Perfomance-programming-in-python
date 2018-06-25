import multiprocessing,os,sys
class multiplicador(multiprocessing.Process):
    def multiplica(self,n):
        return [n*2,os.getpid()]
    



if __name__ == '__main__':
    for i in range(1,len(sys.argv)):
        aux = multiplicador()
        aux.start()
        print(aux.multiplica(int(sys.argv[i])))
    
