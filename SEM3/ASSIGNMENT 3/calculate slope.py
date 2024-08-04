def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return 'Undefined (vertical line)'
    else:
        return (y2 - y1) / (x2 - x1)

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slope = calculate_slope(x1, y1, x2, y2)
print("The slope is: " + str(slope))
