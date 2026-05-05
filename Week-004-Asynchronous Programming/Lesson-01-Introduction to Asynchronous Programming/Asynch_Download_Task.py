# download_file(name) async funksiya yazın
# time.sleep yox, asyncio.sleep istifadə edin
# 3 faylı eyni vaxtda yüklədin
# Nəticələri siyahı kimi çap edin
# Ardıcıl və gather variantını müqayisə edin
import asyncio
async def download_file(name):
    print(f"{name} yüklənir...")
    await asyncio.sleep(2)  
    print(f"{name} yükləndi!")
    return f"{name} nəticəsi"

async def main():
    # Ardıcıl variant
    print("Ardıcıl yükləmə:")
    results = [
        await download_file("Fayl 1"),
        await download_file("Fayl 2"),
        await download_file("Fayl 3")
    ]
    print("Nəticələr:", results)
    # gather variant
    print("\nGather yükləmə:")
    results = await asyncio.gather(
        download_file("Fayl 1"),
        download_file("Fayl 2"),
        download_file("Fayl 3")
    )
    print("Nəticələr:", results)
if __name__ == "__main__":
    asyncio.run(main())