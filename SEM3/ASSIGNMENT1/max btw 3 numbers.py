def find_maximum_of_three(a, b, c):
    if (a >= b) and (a >= c):
        maximum = a
    elif (b >= a) and (b >= c):
        maximum = b
    else:
        maximum = c
    return maximum
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_num = find_maximum_of_three(num1, num2, num3)
print("The maximum of the three numbers is:", max_num)
