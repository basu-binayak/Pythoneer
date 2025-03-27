import asyncio, time 

async def main():
    print(f'{time.ctime()}, Hello!')
    await asyncio.sleep(2.0)
    print(f'{time.ctime()}, Goodbye!')
    
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop) # This gets the current event loop, which is responsible for running asynchronous tasks.
'''
Think of the event loop like a task manager that runs async functions and handles when to pause/resume them.
'''

task = loop.create_task(main()) # This schedules the main() coroutine to run in the event loop.
'''
- main() is turned into a Task.
- It’s ready to be run, but not executed yet.
'''

loop.run_until_complete(task) # This starts the event loop and runs it until the task completes.

'''
So here, it will:
    - Start the main() coroutine
    - Print "Hello!"
    - Wait for 2 second
    - Print "Goodbye!"
    - Then stop
'''

pending = asyncio.all_tasks(loop) # After the main task finishes, this gathers all remaining pending tasks in the event loop.
'''
Usually, this will be an empty set if everything finished correctly. But if there were leftover or background tasks, this would collect them.
'''

for task in pending:
    # Any leftover tasks are now canceled (in case they’re stuck or forgotten)
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
'''
- asyncio.gather() wraps all the pending tasks into one group task.
- return_exceptions=True prevents the loop from crashing if a task throws a CancelledError.
'''

loop.run_until_complete(group) # Now it waits until all canceled tasks finish canceling, ensuring a clean shutdown.

loop.close() # Finally, the event loop is closed, releasing system resources.

'''
NOTE
----
If you use asyncio.run(), none of these steps are necessary: they are all done for you. However, it is important to understand these steps because more complex situations will come up in practice, and you’ll need the extra knowledge to deal with them.
'''
