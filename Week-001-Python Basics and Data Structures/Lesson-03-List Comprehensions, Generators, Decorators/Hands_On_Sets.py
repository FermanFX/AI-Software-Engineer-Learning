# Task 1: Demonstration of Tuple methods
my_tuple = (10, 20, 30, 20, 40, 20)

# count(): Returns the number of times a value appears
print(f"Count of 20: {my_tuple.count(20)}")  # Output: 3

# index(): Returns the first index of a value
print(f"Index of 30: {my_tuple.index(30)}")  # Output: 2

# Task 2: Demonstration of Sets operations and methods
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Basic Methods
s1.add(6)              # Adds 6 to the set
s1.remove(2)           # Removes 2 (raises error if missing)
s1.discard(10)         # Removes 10 if present (no error if missing)

# Mathematical Operations
print(f"Union: {s1 | s2}")                 # Elements in either (or s1.union(s2))
print(f"Intersection: {s1 & s2}")          # Elements in both (or s1.intersection(s2))
print(f"Difference: {s1 - s2}")            # Elements in s1 but not s2
print(f"Symmetric Difference: {s1 ^ s2}")  # Elements in either, but not both
#Task 3
# Define the Universe and Sets
U = set(range(2, 101))
A = {x for x in U if x % 2 == 0}
B = {x for x in U if x % 3 == 0}
C = {x for x in U if x % 5 == 0 or x % 7 == 0}

# a. Multiples of 2 AND 3 (Intersection)
result_a = A & B

# b. Multiples of 2 OR 5 OR 7 (Union)
result_b = A | C

# c. Multiples of 3 that aren't multiples of 5 or 7 (Difference)
result_c = B - C

# d. Multiple of 2 or 3, but not both (Symmetric Difference)
result_d = A ^ B

# e. Complement of multiples of 2, 3, 5, or 7
# This uses the Universe 'U' minus the union of all sets
result_e = U - (A | B | C)

print(f"Solution E (Primes > 7): {sorted(list(result_e))}")



# All Outputs:
# Count of 20: 3
# Index of 30: 2
# Union: {1, 3, 4, 5, 6}
# Intersection: {3}
# Difference: {1, 6}
# Symmetric Difference: {1, 4, 5, 6}
# Solution E (Primes > 7): [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]