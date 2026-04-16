def calculate_series(N):
    terms = []
    tatal_sum = 0
# Iterate from n = 0 to N (inclusive)
    for x in range(N + 1):
 # Calculate the nth term using the formula (3 + 2n) / 2^n
        term = (3+2*x)/(2 ** x)
        terms.append(term)
        tatal_sum += term

    return terms, tatal_sum
# N Tests
N_values= [5,10,100]
for N in N_values:
    term_list, total_sum = calculate_series(N)
    print(f"Terms for N={N}: {term_list}")
    print(f"Total sum for N={N}: {total_sum}\n")
print(f"Terms (first 5): {term_list[:5]}...")