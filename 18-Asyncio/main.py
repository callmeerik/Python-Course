"""
            ASYNCHRONOUS PROGRAMMING
    - Coroutine: a function declared with async key word
    - Await: used inside a coroutine to wait another coroutine to finish
    - Task: a scheduled coroutine
"""
import asyncio

# simulate a task tha consume time
async def fetch_data(delay, id):
    print(f"Coroutine {id}. Starting to fetch date")
    await asyncio.sleep(delay)
    return {"id": id, "data": "Some data fetched"}

# this 👇 is a coroutine
async def main():
    # create tasks
    result1 = await asyncio.create_task( fetch_data(2, 1) )
    result2 = await asyncio.create_task( fetch_data(4, 2) )
    result3 = await asyncio.create_task( fetch_data(6, 3) )

    print(result1)
    print(result2)
    print(result3)

asyncio.run(main())