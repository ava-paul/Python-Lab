def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_series(n):
    prime_series = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_series.append(num)
    return prime_series

n = int(input("Enter a number: "))
prime_series = generate_prime_series(n)
print("Prime number series up to", n, "is:", prime_series)
