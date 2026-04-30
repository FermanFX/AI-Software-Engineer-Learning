import requests

class Telebe:
    def __init__(self, data):
        self.ad = data.get('name')
        self.seher = data.get('address', {}).get('city')
        self.telefon = data.get('phone')
        self.vebsayt = data.get('website')

    def melumati_goster(self):
        print(f"Ad: {self.ad}")
        print(f"Şəhər: {self.seher}")
        print(f"Telefon: {self.telefon}")
        print(f"Vebsayt: {self.vebsayt}")
        print("-" * 20)

class TelebeIdareetme:
    def __init__(self, url):
        self.url = url
        self.telebe_siyahisi = []

    def lazimi_melumatlari_getir(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            istifadeci_data = response.json()
            for data in istifadeci_data:
                yeni_telebe = Telebe(data)
                self.telebe_siyahisi.append(yeni_telebe)
        else:
            print("Məlumat gətirilərkən xəta baş verdi.")

    def gelenler(self):
        for telebe in self.telebe_siyahisi:
            telebe.melumati_goster()

api_url = "https://jsonplaceholder.typicode.com/users"
idareetme = TelebeIdareetme(api_url)

idareetme.lazimi_melumatlari_getir()
idareetme.gelenler()
