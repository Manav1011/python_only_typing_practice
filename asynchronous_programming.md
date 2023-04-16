# Asynchronous Programming

> Asynchronous programming is a programming technique that allows us to execute multiple tasks concurrently without waiting for each task to finish before starting the next one. In traditional synchronous programming, we execute each task in a sequence and wait for each task to complete before starting the next one. In contrast, asynchronous programming enables us to run multiple tasks concurrently, which can result in faster and more efficient code execution.
>
> In Python, the `asyncio` module provides support for asynchronous programming. The `asyncio` module was introduced in Python 3.4 and has since become the preferred way of doing asynchronous programming in Python.
>
> The `asyncio` module uses a cooperative multitasking approach, where tasks are scheduled by the event loop. The event loop is  responsible for managing and executing the coroutines, which are the building blocks of asynchronous programming in Python.
>
> ### **Concepts in asynchronous programming**
>
> * Coroutines
> * Event Loop
> * Tasks
> * Futures
> * Asynchronous I/O
> * Concurrency and Parallelism

## Coroutines

> A coroutine is a special type of function that can be paused and resumed later. Coroutines are defined using the `async def` syntax, which is similar to the `def` syntax used for defining regular functions.
>
> Here's an example of a coroutine that prints a message and waits for 1 second before printing another message:
>
> ```python
> import asyncio
>
> async def hello():
>     print("Hello")
>     await asyncio.sleep(1)
>     print("World")
>
> asyncio.run(hello())
> ```

    Output:

```python
Hello
<1 second delay>
World
```

> In the above example, the `await` keyword is used to pause the coroutine and wait for the `asyncio.sleep(1)` function to complete before resuming the coroutine.
>
> Note that we use `asyncio.run()` to run the coroutine. This function creates a new event loop and runs the coroutine until it completes.
>
> ### Event Loop
>
> The event loop is the central component of the `asyncio` module. It manages and schedules the execution of coroutines, tasks, and callbacks.
>
> The event loop is started using the `asyncio.run()` function. The `run()` function creates a new event loop, runs the coroutine passed to it, and stops the event loop when the coroutine completes.
>
> Here's an example of how to create an event loop and run a coroutine:
>
> ```python
> import asyncio
>
> async def hello():
>     print("Hello")
>     await asyncio.sleep(1)
>     print("World")
>
> loop = asyncio.get_event_loop()
> loop.run_until_complete(hello())
> loop.close()
> ```

Output:

```python
Hello
<1 second delay>
World
```

> In the above example, we create a new event loop using the `asyncio.get_event_loop()` function, run the coroutine using the `run_until_complete()` method of the event loop, and finally close the event loop using the `close()` method.


## Tasks

> A task is a high-level abstraction over a coroutine. It allows us to schedule and execute coroutines concurrently.
>
> We can create a task using the `asyncio.create_task()` function. Here's an example of how to create a task and run it:
>
> ```python
> import asyncio
>
> async def hello():
>     print("Hello")
>     await asyncio.sleep(1)
>     print("World")
>
> async def main():
>     task = asyncio.create_task(hello())
>     await task
>
> asyncio.run(main())
> ```

Output:

```python
Hello
<1 second delay>
World
```
