class Employee:
    def __init__(self, name, salary, mkr_score):
        self.name = name
        self.__salary = salary
        self.__mkr_score = mkr_score

    @property
    def salary(self):
        """Getter: Maaşı oxumaq üçün"""
        return self.__salary

    @salary.setter
    def salary(self, value):
        """Setter: Maaşı təyin etmək üçün (yoxlama ilə)"""
        if value > 0:
            self.__salary = value
        else:
            print("Xəta: Maaş mənfi ola bilməz!")

    @property
    def mkr_score(self):
        """Getter: Balı oxumaq üçün"""
        return self.__mkr_score

    @mkr_score.setter
    def mkr_score(self, value):
        """Setter: Balı təyin etmək üçün"""
        self.__mkr_score = value

    def calculate_final_salary(self):
        score = self.mkr_score
        current_salary = self.salary
        discount_percent = 0

        if 1000 <= score < 2000:
            discount_percent = 40
        elif 2000 <= score < 5000:
            discount_percent = 30
        elif score >= 5000:
            discount_percent = 10
        
        final_amount = current_salary * (1 - discount_percent / 100)
        return final_amount, discount_percent

    def show_info(self):
        final_salary, percent = self.calculate_final_salary()
        print(f"\nİşçi: {self.name}")
        print(f"İlkin Maaş: {self.salary} AZN")
        print(f"MKR Balı: {self.mkr_score}")
        if percent > 0:
            print(f"Tətbiq edilən çıxılma: {percent}%")
            print(f"Yekun ödəniləcək məbləğ: {final_salary} AZN")
        else:
            print("Heç bir çıxılma tətbiq edilmədi.")
            print(f"Yekun Maaş: {self.salary} AZN")


emp1 = Employee("Ferman", 1500, 2500)

emp1.show_info()

emp1.mkr_score = 5500 

emp1.show_info()

emp2 = Employee("Eli", 1500, 2500)

emp2.show_info()

emp2.mkr_score = 5500 

emp2.show_info()
