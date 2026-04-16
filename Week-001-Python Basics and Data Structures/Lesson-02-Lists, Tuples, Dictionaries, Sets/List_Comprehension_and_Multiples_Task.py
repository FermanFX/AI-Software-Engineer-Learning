def multiple_n(n, a=1, b=10):
    return [i for i in range(a, b+1) if i%n==0]
print(multiple_n(4, 1, 12))
print(multiple_n(3))