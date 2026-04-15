# Constant: Gravitational constant
G = 6.674e-11

# Function to calculate force
def calculate_force(m1, m2, r):
    return G * (m1 * m2) / (r**2)

# Case a: Earth and Sun
m1_a = 1.989e30
m2_a = 5.972e24
r_a = 149597870000
force_a = calculate_force(m1_a, m2_a, r_a)

# Case b: Two small objects
m1_b = 70
m2_b = 0.5
r_b = 0.75
force_b = calculate_force(m1_b, m2_b, r_b)

print(f"Force a (Earth/Sun): {force_a:.4e} N")
print(f"Force b (Objects):   {force_b:.4e} N")


# Outputs
# Force a (Earth/Sun): 3.5423e+22 N
# Force b (Objects):   4.1527e-09 N