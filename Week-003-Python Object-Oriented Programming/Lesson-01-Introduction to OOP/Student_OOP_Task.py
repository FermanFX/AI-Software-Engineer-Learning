# 3.) Student class-ı yaradın.
class Student:
# private field-lər:
# __name
# __age
# __grades
# average
    def __init__(self,name,age,grades):
        self.__name = name
        self.__age = age
        self.__grades = grades
        self.__average = self.calculate_average()
    # name property:
    # yalnız string olsun
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string")
    # age property:
    # 16 ilə 30 arasında olmalıdır
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and 16 <= value <= 30:
            self.__age = value
        else:
            raise ValueError("Age must be an integer between 16 and 30")
# grades property:
# yalnız list qəbul etsin
# list içindəki bütün qiymətlər 0 ilə 100 arasında olmalıdır1
    @property
    def grades(self):
        return self.__grades
    @grades.setter
    def grades(self, value):
        if isinstance(value, list):
            for grade in value:
                if not (isinstance(grade, (int, float)) and 0 <= grade <= 100):
                    raise ValueError("All grades must be numbers between 0 and 100")
            self.__grades = value
        else:
            raise ValueError("Grades must be a list")
# average adlı property yaradın
    @property
    def average(self):
        return self.__average
# orta qiyməti qaytarsın
    def calculate_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0
# status adlı  property yaradın
    @property
    def status(self):
         # average >= 90 → "Excellent"
         if self.__average >= 90:
            return "Excellent"
         # average >= 75 → "Good"
         elif self.__average >= 75:
            return "Good"
         # average >= 60 → "Normal"
         elif self.__average >= 60:
            return "Normal"
         # əks halda "Fail"
         else:
            return "Fail"

#Cheching the implementation
student1 = Student("Alice", 20, [85, 90, 78])
print(student1.name)  # Output: Alice
print(student1.age)   # Output: 20
print(student1.grades)  # Output: [85, 90, 78]
print(student1.average)  # Output: 84.33333333333333
print(student1.status)  # Output: Good
student2 = Student("Bob", 22, [92, 88, 95])
print(student2.name)  # Output: Bob
print(student2.age)   # Output: 22
print(student2.grades)  # Output: [92, 88, 95]
print(student2.average)  # Output: 91.66666666666667
print(student2.status)  # Output: Good
