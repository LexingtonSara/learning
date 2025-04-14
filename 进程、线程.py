"""
进程和线程
进程process是操作系统分配资源的最小单位,分配内存;线程thread是操作系统调度的最小单位,调度CPU.
一个进程可以包含多个线程,一个线程只能属于一个进程.这些线程可以分布在多个cpu上执行.
单个cpu在任一时刻只能执行一个线程,cpu在不同线程之间切换,从而实现多任务.只有多核cpu才能真正做到多个线程同时执行.
大多数编程语言中,因为切换消耗的资源更少,多线程比多进程更加高效.
Python是个特例,它使用了全局解释器锁GIL(Global Interpreter Lock),使得多线程更加高效,但也限制了并发性.
GIL规定,在一个进程中每次只能有一个线程在运行,GIL锁相当于线程运行的资格证,然后遇到IO或者超时的时候释放GIL锁,
其他线程才能获得GIL锁并运行,只有获得GIL锁的线程才能执行.
CPU密集型操作使用多进程比较合适,例如海量运算;
IO密集型操作使用多线程比较合适,例如爬虫,文件处理,批量ssh操作服务器等.
"""
# 从主进程创建子进程使用的是Process类,该类在实例化时通常接受两个参数,第一个参数target是要运行的函数,第二个参数args是函数的参数.
# 创建完Process对象后，使用start方法启动该进程，正常情况下，主进程会继续执行直到结束，
# 如果有子进程阻塞，主进程会等待子进程结束后再继续执行，使用join方法让进程阻塞进主进程

from multiprocessing import Process
import time
import os
def func():
    print(f"process {os.getpid()} starts")
    time.sleep(1)
    print(f"process {os.getpid()} ends")

# if __name__ == '__main__':
#     print(f"main process{os.getpid()}starts")
#     start_time = time.time()
#     # func()
#     # func()#执行两次func函数，共用时约total time is 2.0018932819366455s
#     p1 = Process(target=func)
#     p2 = Process(target=func)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()#创建2个子进程，共用时约total time is 1.0709452629089355s
#     end_time = time.time()
#     print(f"total time is {end_time - start_time}s")

    """
    进程的创建和停止需要消耗时间
    因为GIL锁的存在,多线程在同一个进程中只能有一个线程在运行,单个cpu核心只能执行一个线程,最好的情况是进程数量
    和cpu核心数量相同,这样才能充分利用cpu资源,但实际上并不是所有情况都能达到最优,所以多线程还是有其局限性的.
    进程池,一个可容纳最大进程数目的池子,当池子中进程数目不足时自动添加新进程,从而将同时运行的进程数目维持在
    一个上限之内。这里的上限就应该是CPU的核数。
    """
if __name__ == '__main__':
    from multiprocessing import Process,cpu_count,Pool
    print(f"main process is {os.getpid()}")
    print(f"cpu count is {cpu_count()}")#20
    start_time = time.time()
    p=Pool(20)#创建进程池，最大进程数为20
    for i in range(100):#创建100个进程
        p.apply_async(func)#异步执行func函数，不等待func函数执行完毕
    p.close()#关闭进程池，不再接受新的进程
    p.join()#等待进程池中的所有进程执行完毕
    end_time = time.time()
    print(f"total time is {end_time - start_time}s")#total time is 5.269676685333252s
    #进程池是20，一共100个进程，每个进程执行一次func函数，共执行100次，总共耗时5.269676685333252s

    """
    进程间通信
    进程之间是相互独立的,不共享内存空间,所以在一个进程中声明的变量在另一个进程中是看不到的,进程之间进行数据传输,需要借助工具.
    队列(deque)在生产消费者模型中很常见,生产者进程在队列的一端写入数据,消费者进程在另一端读取数据.
    """
from multiprocessing import Process,cpu_count,Pool,Queue
import os,time

def write_to_queue(q):
    for index in range(10):
        print(f"write {index} to queue {q}")
        q.put(index)
        time.sleep(1)
    q.put(None)#结束标识

def read_from_queue(q):
    while True:
        result = q.get(True)#True表示阻塞，直到队列有数据
        if result is None:#结束标识
            break
        print(f"read {result} from queue {q}")

if __name__ == '__main__':
    
    print(f"main process is {os.getpid()}")
    print(f"cpu count is {cpu_count()}")#20
    start_time = time.time()
    print(start_time)
    q = Queue()#创建队列
    p1 = Process(target=write_to_queue,args=(q,))#创建生产者进程
    p2 = Process(target=read_from_queue,args=(q,))#创建消费者进程
    p1.start()#启动生产者进程
    p2.start()#启动消费者进程
    p1.join()
    p2.join()
    end_time = time.time()
    print(end_time)
    print(f"total time is {end_time - start_time}s")

"""
多线程
多线程使用的是threading模块,该模块提供了Thread类,Thread类实例化时接受一个target参数,该参数是要运行的函数,
start方法启动线程,join方法等待线程结束.和Process类用法类似.
线程池
同进程一样,通常视同线程池来自动控制线程数量,因为GIL的存在,多线程在同一个进程中只能有一个线程在运行,线程池没有上限
threading模块是不支持进程池的,但可以使用concurrent.futures模块来统一管理线程和进程池.
"""
# 创建线程池
# from concurrent.futures import ThreadPoolExecutor
# pool=ThreadPoolExecutor(max_workers=20)#创建线程池，最大线程数为20
# pool.submit(func,args)#提交任务到线程池，不等待任务执行完毕
# pool.shutdown(wait=True)#关闭线程池，主线程暂停，等待线程池中的所有任务执行完毕


#创建线程
"""
使用threading模块的Thread类创建线程,Thread类实例化时接受一个target参数和args参数,target参数是要运行的函数,args参数是函数的参数.
程序在执行时,会先创建一个进程,该进程中有一个主线程,如果程序中创建新的线程,主线程会在当前进程内创建子线程
线程的常见方法：
start()：启动子线程,子线程准备就绪,等待CPU调度,具体时间由CPU决定
join()：阻塞，主线程运行到此处,暂停执行主线程,开始执行子线程,直到子线程结束,才继续执行主线程
setDaemon(布尔值)：设置子线程为守护线程,主线程结束时,守护线程也会结束,必须放在start()方法之前调用
setDameon(True),设置为守护线程,主线程执行完毕后,子线程也会自动关闭
setDameon(False),设置为非守护线程,主线程执行完毕后等待子线程,,子线程执行完毕后,子线程才结束
setName(字符串)：设置子线程的名称,start()方法之前调用
getName()：获取子线程的名称
is_alive()：判断线程是否存活

CPU时间片: CPU时间片是指CPU分配给各个线程的时间,每个线程都有自己的时间片,时间片用完后,线程就进入阻塞状态,等待CPU调度
CPU切换线程时,会保存当前线程的状态,切换回之前线程时,会恢复之前线程的状态,从而保证线程切换的效率.但数据可能错乱.
"""   

"""
线程安全
一个进程中可能有多个线程,线程共享所有进程中的资源,如果多个线程同时去操作同一个资源,可能导致数据不一致,称为线程不安全.
两种锁,Lock和Rlock,Lock同步锁,锁一次解一次,如果重复锁就会死锁
Rlock,递归锁,支持多次申请锁和多次释放
threading.Rlock类提供了一种线程安全的方式,通过acquire()和release()方法,可以实现对共享资源的保护,
acquire()方法获取锁,如果锁已经被其他线程获取,则阻塞等待,直到锁被释放,
release()方法释放锁,使得其他线程可以获取锁.
with 锁的对象 语句可以自动获取锁和释放锁,保证线程安全.上下文管理
同一把锁才有意义
"""

"""
死锁
多个线程互相等待对方释放锁,导致程序一直阻塞,称为死锁.
同步锁Lock:重复锁,申请锁和释放锁的次数不一致,导致死锁.
两把锁,互相等待对方释放锁,导致死锁.
"""


#单例模式
# 单例模式是一种常用的设计模式,保证一个类只有一个实例,并提供一个全局访问点.
