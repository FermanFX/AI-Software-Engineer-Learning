from math_utils import TaylorCalculationError, calculate_taylor_step

data_list = [0.5, 0.8, 1.5, -0.2]

try:
    print("Processing list from external module...")
    for index, val in enumerate(data_list):
        # n = index + 1 yazırıq ki, 0-a bölmə olmasın (və ya xətanı görmək üçün dəyişməyin)
        result = calculate_taylor_step(val, index + 1)
        print(f"Index {index}: Result for {val} is {result:.4f}")

except TaylorCalculationError as e:
    print(f"Caught Custom Error: {e}")

except ZeroDivisionError:
    print("Math Error: Division by zero encountered!")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("Execution finished.")