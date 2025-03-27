import asyncio, time

async def main():
    print(f'{time.ctime()}, Hello!')
    await asyncio.sleep(2.0)
    print(f'{time.ctime()}, Goodbye!')
    
asyncio.run(main())

'''
Basic Terminology
------------------
    - async def: defines an asynchronous function (also called a coroutine)
    - await: pauses the coroutine until the awaited result is ready
    - asyncio.run(): runs the main coroutine
    - asyncio.sleep(): an async version of time.sleep() that doesn’t block the whole program
    
'''
    