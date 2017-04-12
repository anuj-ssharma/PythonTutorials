'''
Created on 10-Apr-2017

@author: anuj_
'''
import os

def childProcess():
    print "I am the child process and my PID is: %d"%os.getpid()
    print "the child is exiting"

def parentProcess():
    print "I am the parent process and my PID is: %d"%os.getpid()
    #forking is not supported in Windows ! 
    #childpid = os.fork()
    childpid  = 0
    if childpid == 0:
        childProcess()
    else:
        # we are inside the parent process
        print "We are inside the parent process"
        print "Our child has the PID: %d"%childpid
    
    while True:
        pass


parentProcess()