# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # "olleh"


# 2. Count vowels in a string
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

print(count_vowels("Hello World"))  # 3


# 3. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # True


# 4. Count occurrences of each word in a sentence
def word_count(sentence):
    words = sentence.split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

print(word_count("this is a test this is"))


# 5. Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            result += chr((ord(ch) - ord(base) + shift) % 26 + ord(base))
        else:
            result += ch
    return result

print(caesar_cipher("abc", 3))  # "def"


# 6. Validate email using regex
import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

print(validate_email("test@example.com"))  # True
