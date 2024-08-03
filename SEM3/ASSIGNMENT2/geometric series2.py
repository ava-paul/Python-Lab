import math
def print_factorial_series(N):
    for i in range(1, N + 1):
        print(math.factorial(i))

N = int(input())
print("The first", N, "terms of the factorial series are:")
print_factorial_series(N)
