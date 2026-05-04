import asyncio
import time


async def make_tea():
    print("wait cay ready (2 sec)")
    await asyncio.sleep(2)
    print("Cay ready")

async def make_coffee():
    print(" wait coffee ready(3 sec)")
    await asyncio.sleep(3)
    print("cofee ready")

async def make_sandwich():
    print("wait sandwich ready(4 sec")
    await asyncio.sleep(4)
    print("sandiwitch ready")

async def main():
    start_time = time.perf_counter()
    print("Waiting breakfast\n")

    await asyncio.gather(
        make_tea(),
        make_coffee(),
        make_sandwich()
    )

    end_time = time.perf_counter()
    total_time = end_time - start_time
    
    print(f"\ breakafast was resdy in {total_time:.2f} second️")

if __name__ == "__main__":
    asyncio.run(main())
