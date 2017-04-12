'''
Created on 10-Apr-2017

@author: anuj_
'''

import threading
import Queue
import time



class WorkerThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        print "Thread now running"
        counter = self.queue.get()
        #print counter
        self.queue.task_done()
        print queue.qsize()
    

queue = Queue.Queue()

for j in range(5):
    queue.put(j)

for k in  range(5):
    worker= WorkerThread(queue)
    worker.start()


queue.join()
print "All tasks over"
