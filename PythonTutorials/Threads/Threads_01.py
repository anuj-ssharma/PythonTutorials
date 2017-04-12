import threading
import time


class WorkerThread(threading.Thread):
    
    lock = threading.Lock()
    counter = 0
    
    def __init__(self,lineToPrint):
        threading.Thread.__init__(self)
        self.lineToPrint = lineToPrint
    
    def run(self):
        
        for i in range(5):
            WorkerThread.lock.acquire()
            print self.lineToPrint
            WorkerThread.counter = WorkerThread.counter + 1
            time.sleep(i)
            
            WorkerThread.lock.release()


totalThreads = []
for i in range(5):
    current = WorkerThread("anuj"+str(i))
    totalThreads.append(current)
    current.start()


for t in totalThreads:
    t.join()
    print "Exiting ", t.lineToPrint, " - with counter = ",  WorkerThread.counter