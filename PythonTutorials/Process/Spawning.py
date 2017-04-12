'''
Created on 10-Apr-2017

@author: anuj_
'''
import os

#overlays the parent process i.e. the python interpreter will close
os.execvp("ping", ["ping","127.0.0.1"])

