#Write a program to enter a string. Calculate the length of the string. Find the substring country.
#Count the occurences of each word in the given sentence.
input_string = input("Enter a string: ")
string_length = len(input_string)
print("Length of the string: ", string_length)
if 'country' in input_string:
    print("The substring 'country' is found in the string.")
else:
    print("The substring 'country' is not found in the string.")
word_counts = {}
words = input_string.split()
for word in words:
    word = word.strip(".,!?")
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("Word occurrences in the given sentence:")
for word, count in word_counts.items():
    print(word, ":", count)
