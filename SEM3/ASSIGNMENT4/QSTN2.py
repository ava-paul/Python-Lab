#Write a program that accepts a comma separated sequence of words as input and prints the words
#in a comma-separated sequence after sorting them alphabetically.
input_string = input("Enter a comma-separated sequence of words: ")
words = input_string.split(',')
words.sort()
sorted_string = ','.join(words)
print("Sorted sequence: ", sorted_string)
