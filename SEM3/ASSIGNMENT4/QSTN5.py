#Write a program that accepts a sentence and calculate the number of letters and digits.
input_string = input("Enter a sentence: ")
letters_count = 0
digits_count = 0
for char in input_string:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
print("LETTERS", letters_count)
print("DIGITS", digits_count)
