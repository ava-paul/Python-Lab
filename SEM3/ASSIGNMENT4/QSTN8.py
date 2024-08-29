#write a program which count and print the numbers of each character in a string input by console.
input_string = input("Enter a string: ")
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character counts:")
for char, count in char_count.items():
    print(char, ":", count)
