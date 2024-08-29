#4. Write a program that accepts a sequence of whitespace separated words as input and prints the
#words after removing all duplicate words and sorting them alphanumerically.

input_string = input("Enter a sequence of whitespace-separated words: ")
words = input_string.split()
unique_words = set(words)
sorted_unique_words = sorted(unique_words)
result_string = ' '.join(sorted_unique_words)
print("Sorted unique words:", result_string)
