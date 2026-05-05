# send_email() - 3 saniyə
# save_log() - 1 saniyə
# Hər ikisini create_task ilə başladın
# Sonra await ilə nəticələri gözləyin
# Hansı daha tez bitir, müşahidə edin
import asyncio
async def send_email():
    print("Email göndərilir...")
    await asyncio.sleep(3)  
    print("Email göndərildi!")
    return "Email nəticəsi"

async def save_log():
    print("Jurnal saxlanılır...")
    await asyncio.sleep(1)
    print("Jurnal saxlandı!")
    return "Jurnal nəticəsi"

async def main():
    # Hər iki funksiyanı create_task ilə başladın
    task1 = asyncio.create_task(send_email())
    task2 = asyncio.create_task(save_log())

    # Nəticələri gözləyin
    result1 = await task1
    result2 = await task2

    print("Nəticələr:", result1, result2)

if __name__ == "__main__":
    asyncio.run(main())