def print_geometric_sequence(start, ratio, num_terms):
    for i in range(num_terms):
        term = start * (ratio ** i)
        print(term)

start = 2
ratio = 3
n=int(input())

print("The first", n, "terms of the geometric sequence are:")
print_geometric_sequence(start, ratio, n)
