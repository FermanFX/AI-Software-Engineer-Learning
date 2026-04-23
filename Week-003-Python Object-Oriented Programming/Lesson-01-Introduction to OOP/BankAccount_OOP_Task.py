class BankAccount:

#     Tələblər:

    def __init__(self, owner, balance=0):
        # owner private olsun
        self.__owner = owner
        # balance private olsun
        self.__balance = balance
# balance üçün property yazın
# balance mənfi ola bilməz
    @property
    def balance(self):
        return self.__balance
# balans birbaşa dəyişdiriləndə (acc.balance = ...) yalnız int və ya float qəbul etsin
    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be a number")
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value
# əgər balans 10000-dən çox olarsa ekrana "VIP account" yazsın
        if self.__balance > 10000:
            print("VIP account")
# owner üçün ayrıca property yazın:
    @property
    def owner(self):
        return self.__owner
# ad yalnız hərflərdən ibarət olmalıdır
# minimum 3 simvol olmalıdır
    @owner.setter
    def owner(self, value):
        if not isinstance(value, str):
            raise TypeError("Owner must be a string")
        if len(value) < 3:
            raise ValueError("Owner name must be at least 3 characters long")
        self.__owner = value
# deposit(amount) və withdraw(amount) metodları yazın
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        if self.__balance > 10000:
            print("VIP account")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise GadasiBalanNotEnough("Insufficient balance")
        self.__balance -= amount

# Custom exception sınıfı
class GadasiBalanNotEnough(Exception):
    pass

Person1 = BankAccount("Alice", 5000)
print(Person1.owner)  # Output: Alice
print(Person1.balance)  # Output: 5000
Person1.deposit(6000)  # Output: VIP account
print(Person1.balance)  # Output: 11000

# try-except ilə hata idarəetməsi və istifadəçidən yenidən daxil etmə
print("\n--- Person1 pul çəkmə ---")
while True:
    try:
        amount = float(input("Çəkiləcək məbləği daxil edin: "))
        Person1.withdraw(amount)
        print(f"Uğurlu: {amount} çəkildi. Yeni balans: {Person1.balance}")
        break
    except GadasiBalanNotEnough as e:
        print("Zəhmət olmasa daha az məbləğ çəkmeyi cəhd edin.\n")
    except ValueError as e:
        print("Zəhmət olmasa düzgün məbləği daxil edin.\n")
    except Exception as e:
        print(f"Gözlənilməyan Xəta: {e}\n")

Person2 = BankAccount("Bob", 2000)
print(f"\n--- Person2 ---")
print(Person2.owner)  # Output: Bob
print(Person2.balance)  # Output: 2000

# try-except ilə hata idarəetməsi
print("\n--- Person2 pul çəkmə ---")
while True:
    try:
        amount = float(input("Çəkiləcək məbləği daxil edin: "))
        Person2.withdraw(amount)
        print(f"Uğurlu: {amount} çəkildi. Yeni balans: {Person2.balance}")
        break
    except GadasiBalanNotEnough as e:
        print("Zəhmət olmasa daha az məbləğ çəkmeyi cəhd edin.\n")
    except ValueError as e:
        print("Zəhmət olmasa düzgün məbləği daxil edin.\n")