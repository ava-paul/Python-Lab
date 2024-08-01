def miles_to_kilometers(miles):
    return miles * 1.60934

miles = float(input("Enter distance in miles: "))
kilometers = miles_to_kilometers(miles)
print("The distance in kilometers is:", kilometers)
