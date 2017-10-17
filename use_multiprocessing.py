from multiprocessing import Process
import os 

#the following code is child process will excute
def run_proc(name):
    print('Run child process %s (%s)...'%(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' %os.getpid())
    p = Process(target=run_proc, args=('HHHH',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

##############
##Pool learn

from multiprocessing import Pool 
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds!' %(name, end - start))

if __name__ ==  '__main__':
    print('Parent process is %s.' %os.getpid()) 
    p = Pool(7)
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocessing done...')
    p.close()
    p.join()
    print('All subprocessing Done!')
