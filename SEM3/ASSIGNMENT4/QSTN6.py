#Write a program which accepts a string as input to print “Yes”;
#if the string is “yes” or “YES” or “Yes”, otherwise print “NO”.
input_string = input("Enter a string: ")
if input_string == "yes" or input_string == "YES" or input_string == "Yes":
    print("Yes")
else:
    print("No")
