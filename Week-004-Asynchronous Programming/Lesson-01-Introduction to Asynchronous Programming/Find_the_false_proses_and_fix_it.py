# async def task():
#  time.sleep(2)
#  print("Done")
# async def main():
#  await asyncio.gather(
#  task(), task(), task()
#  )
import asyncio
async def task():
    await asyncio.sleep(2)
    print("Done")

async def main():
    await asyncio.gather(
        task(), task(), task()
    )
if __name__ == "__main__":
    asyncio.run(main())

# False proses is that the original code uses time.sleep instead of asyncio.sleep, which blocks the event loop and prevents other tasks from running concurrently. The fixed code replaces time.sleep with asyncio.sleep, allowing all tasks to run simultaneously without blocking each other.