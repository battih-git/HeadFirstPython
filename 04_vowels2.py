vowels = ['a','e','i','o','u']
word = input("Provide a word to search for a vowel: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(letter)
