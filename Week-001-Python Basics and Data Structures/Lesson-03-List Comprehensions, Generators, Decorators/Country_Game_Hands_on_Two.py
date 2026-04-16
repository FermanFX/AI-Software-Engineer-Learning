# 1. Create the dictionary
capitals_data = {
    "Portugal": "Lisbon",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "Azerbaijan": "Baku",
    "Russia": "Moscow",
    "China": "Beijing",
}

score = 0

# 2. Start the interactive program
print("--- Welcome to the Game of Capitals! ---")

for country, capital in capitals_data.items():
    # Ask the user for input
    user_answer = input(f"What is the capital of {country}? ").lower().strip()
    
    # Check if the answer is correct
    if user_answer == capital.lower():
        print("Correct! Good JOB!")
        score += 1
    else:
        print(f"Wrong Answer. The capital is {capital}.")

# 3. Display final results
print(f"\nGame Over! Your final score: {score}/{len(capitals_data)}")

# Outputs
# --- Welcome to the Game of Capitals! ---
# What is the capital of Portugal? Lisbon
# Correct! Good JOB!
# What is the capital of France? q
# Wrong Answer. The capital is Paris.
# What is the capital of Japan? q
# Wrong Answer. The capital is Tokyo.
# What is the capital of Germany? q
# Wrong Answer. The capital is Berlin.
# What is the capital of Italy? q
# Wrong Answer. The capital is Rome.
# What is the capital of Spain? q
# Wrong Answer. The capital is Madrid.
# What is the capital of United Kingdom? q
# Wrong Answer. The capital is London.
# What is the capital of United States? q
# Wrong Answer. The capital is Washington, D.C..
# What is the capital of Canada? q
# Wrong Answer. The capital is Ottawa.
# What is the capital of Australia? q
# Wrong Answer. The capital is Canberra.
# What is the capital of Azerbaijan? q
# Wrong Answer. The capital is Baku.
# What is the capital of Russia? q
# Wrong Answer. The capital is Moscow.
# What is the capital of China? q
# Wrong Answer. The capital is Beijing.

# Game Over! Your final score: 1/13