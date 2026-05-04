import threading
import time

def send_email():
    print("email göndərilir.")
    time.sleep(2)
    print("email uğurla göndərildi.")

def download_file():
    print("fayl yüklənir")
    time.sleep(2)
    print("Fayl yükləndi.")

def save_log():
    print("loqlar yadda saxlanılır")
    time.sleep(2)
    print("loqlar qeyd edildi.")

t1 = threading.Thread(target=send_email)
t2 = threading.Thread(target=download_file)
t3 = threading.Thread(target=save_log)

start_time = time.time()

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_time = time.time()

print(f"\nBütün proseslər {end_time - start_time:.2f} saniyeye hell olundi.")




