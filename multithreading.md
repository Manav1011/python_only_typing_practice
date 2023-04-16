### Threading

> * Threading is a mechanism in which a program is split into multiple threads, each of which can execute independently. This allows multiple tasks to be performed at the same time, as long as they do not interfere  with each other. Python's threading module provides a way to create and manage threads.
> * Threads are lightweight, independent units of execution that share the same memory space and can communicate with each other. In Python, the `threading` module provides support for creating and managing threads.
>
>   ```python
>   import threading
>
>   def worker():
>       """Thread worker function"""
>       print("Worker thread started")
>       # Do some work here...
>       print("Worker thread finished")
>
>   # Create a new thread
>   thread = threading.Thread(target=worker)
>
>   # Start the thread
>   thread.start()
>
>   # Wait for the thread to finish
>   thread.join()
>
>   print("Main thread finished")
>   ```
>
>   In this example, we define a `worker` function that will be executed in a separate thread. We create a new `Thread` object and pass it the `worker` function as the `target`. We then call the `start` method on the thread object to start the thread, and the `join` method to wait for it to finish.
> * When the `start` method is called, a new thread is created and the `worker` function is executed in that thread. The main thread continues to execute concurrently with the worker thread. When the `worker` function finishes, the thread terminates and the main thread continues execution.
> * Here's an example that demonstrates how to pass arguments to a thread function:
> * ```python
>   import threading
>
>   def worker(name):
>       """Thread worker function"""
>       print("Worker thread started with name", name)
>       # Do some work here...
>       print("Worker thread finished")
>
>   # Create a new thread with an argument
>   thread = threading.Thread(target=worker, args=("Thread 1",))
>
>   # Start the thread
>   thread.start()
>
>   # Wait for the thread to finish
>   thread.join()
>
>   print("Main thread finished")
>
>   ```
>
>   In this example, we define a `worker` function that takes a single argument `name`. We create a new `Thread` object and pass it the `worker` function and an argument tuple containing the name of the thread. We then start the thread and wait for it to finish.
> * When the `worker` function is executed in the thread, it receives the argument `name` that was passed to the `Thread` constructor.
> * Here's an example that demonstrates how to use a `Lock` object to synchronize access to shared resources between threads:
> * ```python
>   import threading
>   def worker(lock, count):
>       """Thread worker function"""
>       for i in range(count):
>           lock.acquire()
>           try:
>               print("Worker thread: ", i)
>               # Do some work here...
>           finally:
>               lock.release()
>
>   # Create a lock object
>   lock = threading.Lock()
>
>   # Create two threads
>   thread1 = threading.Thread(target=worker, args=(lock, 5))
>   thread2 = threading.Thread(target=worker, args=(lock, 5))
>
>   # Start the threads
>   thread1.start()
>   thread2.start()
>
>   # Wait for the threads to finish
>   thread1.join()
>   thread2.join()
>
>   print("Main thread finished")
>
>   ```

> * In this example, we define a `worker` function that takes a `Lock` object and a `count` parameter. The `worker` function uses the lock to synchronize access to a shared resource (in this case, printing to the console). The `Lock` object is acquired before accessing the shared resource and released when finished.
> * We create a `Lock` object and two threads that both execute the `worker` function with the same `Lock` object and a `count`
>   of 5. When the threads start executing, they each acquire the lock before accessing the shared resource, ensuring that only one thread can access it
>
