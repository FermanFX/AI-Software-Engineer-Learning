import requests

class Post:
    def __init__(self, data):
        self.basliq = data.get('title')
        self.mezmun = data.get('body')

    def goster(self):
        print(f"Başlıq: {self.basliq}")
        print(f"Məzmun: {self.mezmun}")
        print("-" * 15)

class TelebeSistemi:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def istifadeci_postlarini_getir(self, user_id):
        response = requests.get(f"{self.base_url}/posts?userId={user_id}")
        
        if response.status_code == 200:
            postlar_data = response.json()
            
            if not postlar_data:
                print(f"\nID-si {user_id} olan istifadəçinin postu tapılmadı.")
                return

            print(f"\n--- ID: {user_id} üçün tapılan postlar ---\n")
            for data in postlar_data:
                yeni_post = Post(data)
                yeni_post.goster()
        else:
            print("Xəta: Məlumat gətirilə bilmədi.")


sistem = TelebeSistemi()

try:
    secilen_id = input("Postlarını görmək istədiyiniz istifadəçi ID-sini daxil edin: ")
    if secilen_id.isdigit():
        sistem.istifadeci_postlarini_getir(secilen_id)
    else:
        print("Zəhmət olmasa düzgün bir rəqəm daxil edin.")
except Exception as e:
    print(f"Gözlənilməz xəta: {e}")
