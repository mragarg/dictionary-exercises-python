user_input = input("Please enter a sentence: ")

user_input = user_input.lower()
words = user_input.split(" ")
word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = 0
    if word in word_count:
        word_count[word] += 1

print(word_count)