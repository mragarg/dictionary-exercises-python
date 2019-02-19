user_input = input("Please enter a word: ")
letter = {}

for char in user_input:
    if char not in letter:
        letter[char] = 0
    if char in letter:
        letter[char] += 1

print(letter)