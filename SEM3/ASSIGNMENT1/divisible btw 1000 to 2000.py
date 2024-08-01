def find_numbers():
    numbers = []
    for i in range(1000, 2001):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)
    return numbers

result = find_numbers()
print("Numbers between 1000 and 2000 that are divisible by 7 but not multiples of 5:")
print(result)
