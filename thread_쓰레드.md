























# Concurrency, Parallelism and Related Terms

"Concurrency는 한번에 여러가지 일을 다루는(deal with) (동시 수행 X) 것이고,
    Parallelism은 동시에(same instance) 여러가지 일을 수행(do) 하는 것"

- Concurrency
- Parallelism
- Process
- Multitasking
- Multiprocessing
- Multiprogramming
- Thread

## Concurrency
컴퓨터공학 문제의 특성 중 하나로 해당 문제를 여러 부분들로 나누는데 쓰임. 각각의 부분을 해결한 후, 최종 결과로 완성

## Sequential Computing
프로세스가 순차적 진행 (하나의 프로세스 종료 후 다른 프로세스 진행)

## Concurrent Computing
기간 내에 여러개의 프로세스가 진행 (동시 실행 X)

## Parallel Computing
동시에 여러개의 프로세스 실행

## 프로세스
Task 또는 실행 인스턴스

## 멀티코어 vs 싱글코어
```
- 멀티코어에서는 여러개의 프로세스가 동시 실행 가능 O
- 싱글코어에서는 여러개의 프로세스가 Sequentially 또는 Concurrently 실행. 동시 실행 불가능 X
    여러프로세스가 번갈아 실행하여 실행 완료 : 여러 프로세스가 동시에 실행 되는 것 처럼 보임. Task 완료가 느릴 수 있음.
```

## Multitasking
Concurrently 실행 (동시실행 X)

## Multiprocessing
멀티코어 환경에서 여러개의 프로세스가 동시 실행

## Multiprogramming
여러개의 프로그램을 메인 메모리에 로드하고,
로딩이 끝나면 프로그램의 프로세스들의 사용가능한 CPU 자원을 이용하여 실행

## Thread
하나의 프로세스는 여러개의 thread(코드 조각)들로 이루어져있음

## Multi-Threading
쓰레드들은 하나의 부모 프로세스 자원을 공유.
```
- 멀티코어 환경에서 하나의 프로세스가 하나의 코어에 할당 됐다면, 해당 프로세스의 쓰레드들은 실행을 위해 이 프로세스를 공유하게 됨.
이것이 쓰레드의 Concurrent 컴퓨팅 입니다.

- 멀티코어 프로세스에서는, 하나의 프로세스에 두개의 쓰레드가 동시에 실행 가능합니다
    , 특히 프로세스가 두개의 코어를 공유할때 parallel 컴퓨팅 이라고 합니다.
```

* Multi-threading
쓰레드로 Concurrent 또는 Parallel 컴퓨팅을 수행 할때 Multi-threading이라고 합니다

## What is a Thread?
프로그램은 보통 프로세스 단위로 실행이 됩니다.
이 프로세스는 여러개의 부분들로 나뉘어 지고 각각은 쓰레드라고 합니다.
문제의 프로세스를 여러개의 쓰레드로 나누는 것과 비슷합니다.

Multi-core processor 컴퓨터는 여러개의 thread를 동시에 실행 할 수 있습니다.
각각의 코어는 한번에 하나의 쓰레드를 처리할 수 있습니다. 따라서 여러개의 쓰레드 처리가 가능합니다.
-> Multi-threading으로 여러개의 task를 동시 처리 가능

Single-core processor 컴퓨터 또한 여러개의 thread 실행이 가능하지만,
동일 physical instance에서 실행은 불가능 하고 concurrent 실행을 합니다 (perceived concurrency)
하나의 쓰레드 일시정지 <-> 다른 쓰레드 실행

```java
public class ProcessorCores {
    public static void main(String[] args){
        // check core(processor) count
        System.out.println(Runtime.getRuntime().availableProcessors());
    }
}
```

## How to create a multi-threaded program using Java?

### Method 01 : Make a child class of the Class java.lang.Thread
```java
import java.lang.Thread; //This explicit import is not required because
                         //java.lang.* is automatically imported by the
                         //system.
 
public class ThreadsDemo extends Thread{
    private int threadNo;
    
    public ThreadsDemo(int num){
        threadNo = num;
    }
    @Override
    public void run(){
        System.out.println("Running thread "+threadNo);
    }
}
```
``` java
public class ThreadsRun {
    public static void main(String[] args){
        ThreadsDemo thrd0 = new ThreadsDemo(0);
        thrd0.start();
        System.out.println("Running thread 1");
        // Running thread 0
        // Running thread 1
        // or
        // Running thread 1
        // Running thread 0


        // thrd0.run(); ---> WILL NOT create new thread and just print in order :
        // Running thread 0
        // Running thread 1
    }
}
```


### Method 02 : Implement java.lang.Runnable Interface

``` java
public class ThreadsRunnable implements Runnable{
 
    private int threadNo;
    
    public ThreadsRunnable(int num){
        threadNo = num;
    }
    @Override
    public void run(){
        System.out.println("Running thread "+threadNo);
    }
}

```

```java
public class ThreadsRun {
    public static void main(String[] args){
        //Create a new ThreadsRunnable Object “demo”.
        ThreadsRunnable demo = new ThreadsRunnable(0);
 
        //pass the object “demo” as a parameter to a 
        //new Thread object t.
        Thread t = new Thread(demo);
 
        //start a new thread by calling t.start();
        t.start();
        System.out.println("Running thread 1");
    }
}
```



## Basic Operations on Threads

- Thread.sleep(long milliseconds)
- t.interrupt()
- t.join()
- t.join(long milliseconds)

t1이 쓰레드이고 이 쓰레드 메소드를 t2쓰레드에서 call하는 상황 가정.
```
// t.join()
t2쓰레드{
    try{
        // t 쓰레드가 완료될때 까지 t2 sleep
        // t 이 execution을 끝낸 뒤에 t2 run
        t.join();
    } catch(Exception e){
        e.printStackTrace();
    }
}
// t.join(long miliseconds)
// t2 쓰레드는 miliseconds 이후에 wake up (t 쓰레드 dead 여부와 상관없이)
// miliseconds가 지나기 전에 t가 실행 stop 한다면, t2쓰레드 run
```

``` java
try {
    x1.join();
    x2.join();
} catch (InterruptedException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}
```

### Example of using several threads at once
``` java
import java.util.ArrayList;
 
public class PrimesCounter extends Thread{
	
	private int id;
	
	public PrimesCounter(int id){
		this.id = id;
	}
	
	public void run(){
		
		long startTime = System.currentTimeMillis();
		int count = countPrimes(5000000);
		long elapsedTime = System.currentTimeMillis()-startTime;
		System.out.println("The thread "+id+" took "+(elapsedTime/1000.0)+" seconds"
				+ " and counted "+count+" primes");
	}
	
	private static int countPrimes(int val) {
		
		ArrayList primes = new ArrayList();
		
		boolean isPrime=true;
		for (int i=3;i<=val;i++){
			if (isPrime)
				primes.add(i-1);
			int j=0;
			int sqrVal = (int) Math.sqrt(i);
			sup:for (;j<primes.size();j++){ int div = primes.get(j); if (div>sqrVal){
					isPrime=true;
					break sup;
				}
				if (i%(primes.get(j))==0){
					isPrime=false;
					break sup;
				}
				
			}
		}
		return primes.size();
	}
 
	public static void main(String[] args){
		int range = 4;
		PrimesCounter[] worker = new PrimesCounter[range];
		long startTime = System.currentTimeMillis();
		for(int i=0;i<range;i++){
			worker[i] = new PrimesCounter(i+1);
			worker[i].start();
		}
		for(int i=0;i<range;i++){
			try {
				worker[i].join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		long elapsedTime = System.currentTimeMillis() - startTime;
		System.out.println("Total elapsed time: " + (elapsedTime/1000.0) + " seconds");
        // The thread 3 took 1.43 seconds and counted 348513 primes
        // The thread 4 took 1.49 seconds and counted 348513 primes
        // The thread 1 took 1.563 seconds and counted 348513 primes
        // The thread 2 took 1.604 seconds and counted 348513 primes
        // Total elapsed time: 1.604 seconds
	}
}
```
## Race Condition
여러개의 쓰레드가 동시에 하나의 task를 실행하려고 할때 발생.
하나의 프로그램은 여러개의 파트들(쓰레드)로 나뉘어 집니다.
즉 프로그램의 component를 쓰레드들이 공유할 수 있습니다


## Synchronization
Mutual Exclusion : 레이스 컨디션 문제 해결 'synchronized'

1. synchronized methods

``` java
public class Counter {
    private int tot;

    synchronized public void setTotal(int val){
        tot+=val;
    }
    synchronized public int getTotal(){
        return tot;
    }
 }
```

``` java
public static void main(String[] args) {
    // Counter 객체는 모든 쓰레드들에 의해 공유 됨
    // 'synchronized' 키워드는 쓰레드가 해당 키워드 메소드를 호출 할때,
    // 이 쓰레드만 객체에 접근할 수 있도록 합니다
    Counter total = new Counter();
    total.setTotal(10);

    if(total.getTotal() <= 1000) {
        // do something with total
    }
}
```

2. synchronized statement
``` java
// synchronized(object){}
synchronized(total){
    if (total.getTotal()<=1000){
        //do something with total
    }
}
```

## Deadlocks
쓰레드 t1은 synchronized 된 변수 A를 가지고 있고,
쓰레드 t2은 synchronized 된 변수 B를 가지고 있는 상황

t1은 실행을 위해 B가 필요하고, t2는 A가 필요한 상황이라면,
A는 t2가 접근 할 수 없고, B도 t1이 접근 불가능하므로, 두개의 쓰레드가 영원히 sleep
=> careful multi thread implementation is required

## Volatile Variables
``` java
private volatile int x;
```
```
변수 x가 2개의 쓰레드에 의해 공유되고 있고, 이 쓰레드들이 2개의 프로세서에서 실행 되는 상황 가정.
각각의 프로세서는 built-in 메모리를 가지고 있어서, 시스템은 쓰레드와 관련있는 변수를 이 메모리에 저장 합니다.

하나의 쓰레드가 x값을 바꾸면, 다른 하나의 쓰레드는 x에 대한 캐쉬메모리가 다르기 때문에 이 변화를 볼 수 없습니다.
이런 문제를 피하고, 성공적인 thread-to-thread 커뮤니케이션을 위해, volatile 변수를 사용합니다

volatile 키워드는 쓰레드가 변수 x에 대한 캐시메모리를 저장하지 말아야 한다는 것을 명시
따라서, 쓰레드들은 x에 대해 직접적인 접근이 가능하며, 가장 최신의 값을 받을 수 있음
다만, volatile 변수들로 race컨디션 해결 불가능. 앞에서 언급했듯이, synchronization으로 race컨디션을 해결해야 합니다.
```


# What are Thread Pools in Java?


## New problem...
이전과 같이 4개의 thread가 각 sub problem들을 4개의 프로세서에서 동시에 (parallel-programming)처리하는 상황.
만약 3개의 thread는 task를 마쳤고, B task는 복잡해서 해당 쓰레드가 작업을 수행 중이라면, 나머지 3개의 프로세서는 idle상태가 됨
: waste of resources
: task B is sub divided into B1 B2 B3 B4
프로세서가 idle상태가 되는 순간 이 sub problem들을 실행하여 resource fully 활용


## How to handle these sub-problems?
Example
```java
int range = imageRows;
ImageProcessingThread[] workers = new ImageProcessingThread[range];
// Suppose ImageProcessingThread(int rowNo); is a Thread object that contgains the sub-task
// to process the row having the number rowNo in an image. so, for all rows

for(int i =0; i<range; i++){
    workers[i] = new ImageProcessingThread(i+1);
    workers[i].start();
}

// So in 1366×768 image, 768 WorkerThreads
// 여기서도 각각의 쓰레드는 한번만 쓰일 것이고, 각 task를 끝내면 쓰레드가 제거됨
// : wasteful! -> use Thread Pool!
for(int i =0; i<range; i++){
    try{
        workers[i].join();
    } catch(InterrupedException e) {
        e.printStatckTrace();
    }
}
```

## So, can you think about a better approach?
위의 예제처럼, sub-task들을 각 쓰레드들에 넣는 방법 대신에, 적은 수의 쓰레드로 이루어진 'pool'과 sub-task 리스트를 준비합니다.


이 리스트의 모든 sub-task들이 끝날때 까지, 'pool'에 있는 쓰레드들은 제거되지 않습니다.
'pool'에 있는 각각의 쓰레드는 처음에 list로 부터 sub-task를 부여 받습니다.
thread의 sub-task가 끝나면, 남은 sub-task로부터 새로운 task를 쓰레드에 assign 합니다.
모든 sub-task들이 끝날때 까지 이 과정을 반복합니다. 이 방법은 768개의 쓰레드를 생성하고 destroy하는 프로세스로 인한 자원 낭비를 피할 수 있게 합니다.


## Now, how do we direct sub-tasks to the thread pool?
타입을 가진 배열에 768개의 sub-task 객체들을 넣습니다. 이 배열은 'queue'와 같은 기능 합니다.

쓰레드 pool에 새로운 sub-task를 넣을 자리가 생기면, queue로 부터 아이템이 pop 됩니다.
``` java
// sub-task 리스트를 taskQueue 변수에 저장
ConcurrentLinkedQueue<Runnable> taskQueue = new ConcurrentLinkedQueue<Runnable>();

// 어떤 수의 sub-task들이든 이 taskQueue에 들어갈 수 있습니다
// 물론 subTask는 Runnable 인터페이스를 implement하는 객체여야 합니다.
taskQueue.add(subTask);
```

![Thread Pool](https://i0.wp.com/www.geek-programmer.com/wp-content/uploads/2017/07/thread_pool_and_task_queue.png?w=745&ssl=1)



### Thread pool-how it works
쓰레드 pool을 사용 하기 위한 steps :

1. Runnable 인터페이스를 implement하는 sub-task 클래스 생성
2. ConcurrentLinkedQueue 객체를 만들어서 sub-task 객체를 넣음
3. 쓰레드 pool을 위한 Thread 배열 생성
``` java
import java.util.concurrent.ConcurrentLinkedQueue;

public class ThreadInThePool extends Thread{
    ConcurrentLinkedQueue<Runnable> taskQueue;

    private boolean isRunning=true;

    public ThreadInThePool(ConcurrentLinkedQueue<Runnable> queue){
        taskQueue=queue;
    }

    //this will stops the loop in the run() method before finishing
    //all sub-tasks in the taskQueue.
    public void abort(){
        isRunning = false;
    }

    public void run(){
        while(isRunning){
            Runnable subTask=taskQueue.poll();
            if(subTask==null){
                break; //break statement terminates the thread when all the sub-tasks
                //in the taskQueue are over!
            }
            subTask.run();
        }
    }
 }
```

```abort()``` 메소드는 run상태의 Thread 객체를 중단시키고, Thread pool에서 제거하는 메소드

```run()``` 메소드에서 subTask들을 run(). 각각의 subTask의 run() 메소드가 완료되면, task queue로부터 새로운 sub-task를 요청.
이 과정이 task queue가 empty가 될 때 까지 반복하고, empty가 되면 thread가 종료.


### Example Without Using Above Concepts
``` java
// count the number of primes between 1~10000000
public class CountPrimes implements Runnable{
 
    int count = 0;
    int min,max;
    public CountPrimes(int min,int max) {
        this.min = min;
        this.max = max;
    }
 
    public int getCount(){
        return count;
    }
 
    private static boolean isPrime(int val){
        int sqr = (int)Math.sqrt(val);
        for(int i=2;i<=sqr;i++){
            if (val%i==0)
                 return false;
 
        }
        return true;
    }
 
    @Override
    public void run() {
        for (int i = min; i<=max;i++){
            if(isPrime(i))
            count++;
        }
 
    }
 
    public static void main(String[] args){
        long startTime = System.currentTimeMillis();
        CountPrimes n=new CountPrimes(1,10000000);
        n.run();
        long elapsedTime = System.currentTimeMillis() - startTime;
        System.out.println(n.getCount());
        System.out.println("Total elapsed time: " + (elapsedTime/1000.0) + " seconds");
    }
}
```


### Example Using Above Concepts
considerably smaller elapsed time than the previous time.
``` java
import java.util.concurrent.ConcurrentLinkedQueue;
 
    public class ThreadInThePool extends Thread{
    ConcurrentLinkedQueue<Runnable> taskQueue;
 
    private boolean isRunning = true;
    private int ct = 0;
 
    private static int thrdCt=0;
    private static int total = 0;
    private static long startTime,elapsedTime;
 
    public ThreadInThePool(ConcurrentLinkedQueue<Runnable> queue){
        taskQueue=queue;
    }
 
    //this will stops the loop in the run() method before finishing
    //all sub-tasks in the taskQueue.
    public void abort(){
        isRunning = false;
    }
 
    public void run(){
        try{
            while(isRunning){
                Runnable subTask=taskQueue.poll();
 
                if(subTask==null){
                    break; //break and the thread terminates when all the sub-tasks
                    //in the taskQueue are over!
                }
                subTask.run();
                CountPrimes tsk = (CountPrimes) subTask;
                ct+=tsk.getCount();
            }
            addToTotal(ct);
 
        }
        finally{
            increseThrdCt();
            if (thrdCt==8){
                System.out.println(total);
                elapsedTime= System.currentTimeMillis() - startTime;
                System.out.println("Total elapsed time: " + (elapsedTime/1000.0) + " seconds");
 
            }
        }
    }
 
    synchronized private static void increseThrdCt(){
        thrdCt++;
    }
 
    synchronized private static void addToTotal(int x) {
        total = total + x;
    }
 
    public static void main(String[] args){
        startTime = System.currentTimeMillis();
        ConcurrentLinkedQueue<Runnable> queue = new ConcurrentLinkedQueue<Runnable>();
        int lo = 1;
        int hi = 10000000/20;
 
        for (int i=0;i<20;i++){
            CountPrimes obj = new CountPrimes(lo,hi);
            queue.add(obj);
            lo = hi;
            hi = hi+10000000/20;
 
        }
 
        ThreadInThePool[] thrdPool = new ThreadInThePool[8];
        for (int i=0;i<8;i++){
            thrdPool[i] = new ThreadInThePool(queue);
            thrdPool[i].start();
        }
    }
 }
```