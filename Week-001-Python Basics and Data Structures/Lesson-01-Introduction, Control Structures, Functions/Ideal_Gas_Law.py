# Constants from the slide
R = 8.31446261815324  # Ideal gas constant (J⋅K^(-1)⋅mol^(-1))
n = 1                 # Number of moles

def calculate_gas_law():
    print("--- Ideal Gas Law Calculations ---")

    # 1. Calculate Pressure (P)
    # Given: V = 0.25 m^3, T = 300 K
    v1, t1 = 0.25, 300
    p1 = (n * R * t1) / v1
    print(f"1. Pressure (P) for V={v1} and T={t1}: {p1:,.2f} Pa")

    # 2. Calculate Volume (V)
    # Given: P = 500 Pa, T = 321 K
    p2, t2 = 500, 321
    v2 = (n * R * t2) / p2
    print(f"2. Volume (V) for P={p2} and T={t2}: {v2:.4f} m³")

    # 3. Calculate Temperature (T)
    # Given: P = 2.5x10^3 Pa, V = 1x10^(-5) m^3
    p3, v3 = 2.5e3, 1e-5
    t3 = (p3 * v3) / (n * R)
    print(f"3. Temperature (T) for P={p3} and V={v3}: {t3:.6f} K")

if __name__ == "__main__":
    calculate_gas_law()




# Outputs
# --- Ideal Gas Law Calculations ---
# 1. Pressure (P) for V=0.25 and T=300: 9,977.36 Pa
# 2. Volume (V) for P=500 and T=321: 5.3379 m³
# 3. Temperature (T) for P=2500.0 and V=1e-05: 0.003007 K
