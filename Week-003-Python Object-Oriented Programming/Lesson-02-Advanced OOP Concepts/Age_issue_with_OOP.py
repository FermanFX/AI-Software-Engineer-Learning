class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 100:
            self.__age = value
        else:
            print("Uzun ömürlüler qebul olunmur :)))")

    def get_birth_year(self):
        current_year = 2026 
        birth_year = current_year - self.__age 
        return birth_year

    def info(self):
        print(f"Ad: {self.name}")
        print(f"Yaş: {self.age}")
        print(f"Doğum ili: {self.get_birth_year()}")

s1 = Student("Ferman", 22)
s1.info()
