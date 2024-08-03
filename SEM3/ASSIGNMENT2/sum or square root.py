import math

def sum_of_square_roots(a, b, c):
    # Calculate the square roots
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)
    sqrt_c = math.sqrt(c)
    
    # Sum the square roots
    result = sqrt_a + sqrt_b + sqrt_c
    
    return result

# Example usage
num1 = 4
num2 = 16
num3 = 25

print("The sum of the square roots is:", sum_of_square_roots(num1, num2, num3))
