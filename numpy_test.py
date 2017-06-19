# import numpy as np
# a=np.arange(10)
# print(a)
# print(a[0:-1])
# print(a[:-1])
# print(a[::-1])
# print(a[1:5:-1])
# print(a[5::-1])
# import tkinter
# top=tkinter.Tk()
# top.mainloop()
from multiprocessing import Pool
import os, time, random

def long_time_task():
    i=1
    while True:
        i=i+1

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')