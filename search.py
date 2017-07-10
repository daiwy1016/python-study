from multiprocessing import Process,Pool
import os,time,random
try:
    import cPickle as pickle
except:
    import pickle

def search(kw,dir=os.path.abspath('.')):
    for i in os.listdir(dir):
        path=os.path.join(dir,i)
        if os.path.isfile(path) and kw in i:
            print path
        if os.path.isdir(path):
            search(kw,path)
            
#search('work')
#d= dict(name='b',age=20,score=88)
#pickle.dumps(d)
def run_proc(name):
    print 'run child process %s(%s)'%(name,os.getpid())

def long_time_task2(name):
    print 'Run task %s (%s)...' % (name,os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'task %s run %0.2f seconds' % (name,(end - start))
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
if __name__=='__main__':
    print 'parent process %s'%os.getpid()
    #p=Process(target=run_proc,args=('test',))
    p=Pool()
    for i in range(5):
        p.apply_async(long_time_task2,args=(i,))
    print 'process will start'
    #p.start()
    p.close()
    p.join()
    print 'process end.'