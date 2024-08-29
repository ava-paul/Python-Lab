'''9.Write a program that accepts a string
I. 1.reverses it.
II. 2.checks whether it is a palindrome.
III. 3.checks whether it ends with a specific substring.
IV. 4.capitalize the first letter of each word in a string
V. 5.check if a string is anagram of another string
VI. 6.remove vowels from string
VII. 7.find length of the longest word in a sentence'''

def reverse_string(s):
    return s[::-1]
def is_palindrome(s):
    return s == s[::-1]
def ends_with(s, substring):
    return s.endswith(substring)
def capitalize_first_letter(s):
    return s.title()
def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])
def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words)
a = input("Enter a string: ")
substring = input("Enter a substring to check if the string ends with it: ")
b = input("Enter another string to check for anagram: ")
print("Reversed string:", reverse_string(a))
print("Is the string a palindrome?", is_palindrome(a))
print(f"Does the string end with ",substring,"?", ends_with(a, substring))
print("String with first letter of each word capitalized:", capitalize_first_letter(a))
print(f"Is the string an anagram of ",b,"?", is_anagram(a, b))
print("String with vowels removed:", remove_vowels(a))
print("Length of the longest word in the sentence:", longest_word_length(a))
