'''
Created on 10-Apr-2017

@author: anuj_
'''

#I Have added a few comments to this


import thread
import time

def workerThread(id):
    print "Thread %d is now alive"%id
    count = 1
    while True:
        print "Thread with ID %d has counter value %d"% (id,count)
        time.sleep(2)
        count += 1

for i in range(5):
    thread.start_new_thread(workerThread, (i,))


print "Main thread going for a infinite wait loop"
while True:
    pass