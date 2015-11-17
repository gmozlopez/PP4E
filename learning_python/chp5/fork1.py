"forks child process until you type q"

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0) # else go back to the parent loop

def parent():
    while True:
        newpid= os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q': break

parent()