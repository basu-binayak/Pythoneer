import asyncio, time

async def main():
    print(f'{time.ctime()} Hello!')
    
    # Run blocking() in a separate thread but DON'T await it yet
    task = asyncio.create_task(asyncio.to_thread(blocking))
    
    await asyncio.sleep(2.0)
    print(f'{time.ctime()} Goodbye!')
    
    # Optionally wait for blocking() to finish (if not already)
    await task
    
def blocking():
    time.sleep(1.0)
    print(f"{time.ctime()} Hello from a thread!")

# Recommended entry point for async programs
asyncio.run(main())

'''
NOTE: Consider the following code 
'''

async def main():
    print(f'{time.ctime()} Hello!')
    
    # Run the blocking code in the background
    await asyncio.to_thread(blocking)
    
    await asyncio.sleep(2.0)
    print(f'{time.ctime()} Goodbye!')
    
def blocking():
    time.sleep(1.0)
    print(f"{time.ctime()} Hello from a thread!")

# Entry point
asyncio.run(main())

'''
O/P

Thu Mar 27 12:51:34 2025 Hello!
Thu Mar 27 12:51:35 2025 Hello from a thread!
Thu Mar 27 12:51:37 2025 Goodbye!

❓ So Why Does It Wait 2 Seconds After the Blocking?
-----------------------------------------------------
That’s because asyncio.to_thread(blocking) is an awaitable — it waits for blocking() to finish in the background thread before continuing to the next line (await asyncio.sleep(2.0)).

🔄 Think of it like this:

[ Start main() at t = 0 ]
→ Print "Hello!" immediately
→ Start blocking() in thread
→ Wait for blocking() to finish (1 sec)
→ Print "Hello from a thread!"
→ Sleep for 2 seconds
→ Print "Goodbye!" (at t = 3s)

NOTE:
Even though blocking() is run in a thread (so it doesn’t block the event loop), you are awaiting its result, so it still delays the next line until the blocking call completes.

If you want the blocking task to run in parallel and not await it immediately, you could create_task() around it.
'''