def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["yes", "no"]:
            return value
        else:
            print("Please enter only 'yes' or 'no'!")

def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                print("Age cannot be negative!")
            else:
                return age
        except ValueError:
            print("Please enter a valid number!")

age = get_age()

# Category
if age < 24:
    category = "YOUNG"
elif age < 60:
    category = "MIDDLE-AGE"
else:
    category = "SENIOR"


if category == "YOUNG":
    is_student = get_yes_no("Is student? (yes/no): ")
    result = "APPROVED" if is_student == "yes" else "DENIED"

elif category == "MIDDLE-AGE":
    result = "APPROVED"

else:  
    is_excellent = get_yes_no("Is credit rating excellent? (yes/no): ")
    result = "APPROVED" if is_excellent == "yes" else "DENIED"

print(f"Application Result: {result}")