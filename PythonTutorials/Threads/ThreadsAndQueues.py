'''
Created on 10-Apr-2017

@author: anuj_
'''
from logging import thread
from ctypes.test.test_errno import threading

'''
Create task queues
Threads recieve tasks
Threads complete tasks and inform the queue
All threads exit once queue is empty
'''

import threading
import Queue
import time

class WorkerThread(threading.Thread):
    def __init__(self,queue,i):
        threading.Thread.__init__(self)
        self.queue = queue
        self.i = i
    
    def run(self):
        print "In worker thread"
        print self.i
        while True:
            counter = self.queue.get()
            print 'Thread  ordered to sleep for %d seconds'%counter
            time.sleep(counter)
            print 'Thread Finished sleeping for %d seconds'%counter
            self.queue.task_done()


queue = Queue.Queue()

for i in range(10):
    print 'Creating worker thread: %d'%i
    worker = WorkerThread(queue,i)
    worker.setDaemon(True)
    worker.start()
    print 'Worker Thread %d created\n'%i

for j in range(5):
    queue.put(j)

queue.join()
print "All tasks over"
