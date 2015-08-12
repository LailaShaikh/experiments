from multiprocessing import Process,Queue
from multiprocessing.pool import ThreadPool

def func1():
   l = 0
   for i in xrange(10000000):
       l+= i
       #print 'llll',l
   return l

def func2():
   k = 0
   for i in xrange(10000000):
       k += 1
       #print 'kkkkk',k
   return k

if __name__ == '__main__':
   # manager = Manager()
   # return_dict = manager.dict()
   import time
   t = time.time()
   
   """
   func1()
   func2()

   print time.time() - t
   """
   


   #"""
   p = Process(target=func1)
   p1 = Process(target=func2)
   p.start()
   p1.start()
   p.join()
   p1.join()
   print time.time() - t
   #"""
