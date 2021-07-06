.. currentmodule:: asyncio


====================
Coroutines and Tasks
====================

This section outlines high-level asyncio APIs to work with coroutines
and Tasks.

.. contents::
   :depth: 1
   :local:


.. _coroutine:

Coroutines
==========

:term:`Coroutines <coroutine>` declared with the async/await syntax is the
preferred way of writing asyncio applications.  For example, the following
snippet of code (requires Python 3.7+) prints "hello", waits 1 second,
and then prints "world"::

    >>> import asyncio

    >>> async def main():
    ...     print('hello')
    ...     await asyncio.sleep(1)
    ...     print('world')

    >>> asyncio.run(main())
    hello
    world

Note that simply calling a coroutine will not schedule it to
be executed::

    >>> main()
    <coroutine object main at 0x1053bb7c8>

To actually run a coroutine, asyncio provides three main mechanisms:

* The :func:`asyncio.run` function to run the top-level
  entry point "main()" function (see the above example.)

* Awaiting on a coroutine.  The following snippet of code will
  print "hello" after waiting for 1 second, and then print "world"
  after waiting for *another* 2 seconds::

      import asyncio
      import time

      async def say_after(delay, what):
          await asyncio.sleep(delay)
          print(what)

      async def main():
          print(f"started at {time.strftime('%X')}")

          await say_after(1, 'hello')
          await say_after(2, 'world')

          print(f"finished at {time.strftime('%X')}")

      asyncio.run(main())

  Expected output::

      started at 17:13:52
      hello
      world
      finished at 17:13:55

* The :func:`asyncio.create_task` function to run coroutines
  concurrently as asyncio :class:`Tasks <Task>`.

  Let's modify the above example and run two ``say_after`` coroutines
  *concurrently*::

      async def main():
          task1 = asyncio.create_task(
              say_after(1, 'hello'))

          task2 = asyncio.create_task(
              say_after(2, 'world'))

          print(f"started at {time.strftime('%X')}")

          # Wait until both tasks are completed (should take
          # around 2 seconds.)
          await task1
          await task2

          print(f"finished at {time.strftime('%X')}")

  Note that expected output now shows that the snippet runs
  1 second faster than before::

      started at 17:14:32
      hello
      world
      finished at 17:14:34


.. _asyncio-awaitables:

Awaitables
==========

We say that an object is an **awaitable** object if it can be used
in an :keyword:`await` expression.  Many asyncio APIs are designed to
accept awaitables.

There are three main types of *awaitable* objects:
**coroutines**, **Tasks**, and **Futures**.


.. rubric:: Coroutines

Python coroutines are *awaitables* and therefore can be awaited from
other coroutines::

    import asyncio

    async def nested():
        return 42

    async def main():
        # Nothing happens if we just call "nested()".
        # A coroutine object is created but not awaited,
        # so it *won't run at all*.
        nested()

        # Let's do it differently now and await it:
        print(await nested())  # will print "42".

    asyncio.run(main())

.. important::

   In this documentation the term "coroutine" can be used for
   two closely related concepts:

   * a *coroutine function*: an :keyword:`async def` function;

   * a *coroutine object*: an object returned by calling a
     *coroutine function*.


.. rubric:: Tasks

*Tasks* are used to schedule coroutines *concurrently*.

When a coroutine is wrapped into a *Task* with functions like
:func:`asyncio.create_task` the coroutine is automatically
scheduled to run soon::

    import asyncio

    async def nested():
        return 42

    async def main():
        # Schedule nested() to run soon concurrently
        # with "main()".
        task = asyncio.create_task(nested())

        # "task" can now be used to cancel "nested()", or
        # can simply be awaited to wait until it is complete:
        await task

    asyncio.run(main())


.. rubric:: Futures

A :class:`Future` is a special **low-level** awaitable object that
represents an **eventual result** of an asynchronous operation.

When a Future object is *awaited* it means that the coroutine will
wait until the Future is resolved in some other place.

Future objects in asyncio are needed to allow callback-based code
to be used with async/await.

Normally **there is no need** to create Future objects at the
application level code.

Future objects, sometimes exposed by libraries and some asyncio
APIs, can be awaited::

    async def main():
        await function_that_returns_a_future_object()

        # this is also valid:
        await asyncio.gather(
            function_that_returns_a_future_object(),
            some_python_coroutine()
        )

A good example of a low-level function that returns a Future object
is :meth:`loop.run_in_executor`.


Running an asyncio Program
==========================

.. function:: run(coro, *, debug=False)

    Execute the :term:`coroutine` *coro* and return the result.

    This function runs the passed coroutine, taking care of
    managing the asyncio event loop, *finalizing asynchronous
    generators*, and closing the threadpool.

    This function cannot be called when another asyncio event loop is
    running in the same thread.

    If *debug* is ``True``, the event loop will be run in debug mode.

    This function always creates a new event loop and closes it at
    the end.  It should be used as a main entry point for asyncio
    programs, and should ideally only be called once.

    Example::

        async def main():
            await asyncio.sleep(1)
            print('hello')

        asyncio.run(main())

    .. versionadded:: 3.7

    .. versionchanged:: 3.9
       Updated to use :meth:`loop.shutdown_default_executor`.

    .. note::
       The source code for ``asyncio.run()`` can be found in
       :source:`Lib/asyncio/runners.py`.
