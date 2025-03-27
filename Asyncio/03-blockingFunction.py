import asyncio, time

async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(2.0)
    print(f'{time.ctime()} Goodbye!')

# define the blocking function 
def blocking():
    '''
    This is a normal synchronous function that sleeps for 1 second, then prints a message. If you called this directly in the event loop, it would block the entire program.
    '''
    time.sleep(1.0)
    print(f"{time.ctime()} Hello from a thread!")

# start the event loop and the main task 
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop) 

task = loop.create_task(main())

# run blocking() in a separate thread 
loop.run_in_executor(None, blocking)
'''
This tells the event loop:
    "Run this function in a background thread so it doesn't block the loop."

- None uses the default ThreadPoolExecutor
- Now blocking() runs in parallel with your async tasks!
'''

# run the event loop 
loop.run_until_complete(task) # Starts the event loop and waits until main() is finished. Meanwhile, blocking() is running concurrently in a thread.

# cancel the pending tasks 
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

# clean up remaining tasks 
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()



