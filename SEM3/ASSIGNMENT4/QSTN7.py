#Write a program which accepts a sequence of words separated by whitespace as input to print the
#words composed of digits only.
# Input the sequence of words
input_string = input("Enter a sequence of words separated by whitespace: ")
words = input_string.split()
digit_words = [word for word in words if word.isdigit()]
print(digit_words)
