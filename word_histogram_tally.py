user_input = input("Please enter a sentence: ")

user_input = user_input.lower()
words = user_input.split(" ")
word_count = {}

#For loop creates a tally of how many times a word occurs in the sentence
for word in words:
    if word not in word_count:
        word_count[word] = 0
    if word in word_count:
        word_count[word] += 1

#Creates a new dictionary that contains the same contents of word count
word_count_tally = word_count

#While loop only goes up for three values because we are trying to find the top three words
count = 0
while count < 3:
    #Uses max() function to determine what is the max count in the dictionary
    max_count = max(word_count_tally, key=word_count_tally.get)

    #Prints out the max value that is found after each iteration of the while loop
    print("%s: %d" % (max_count, word_count_tally[max_count]))
    
    #deletes the max count value from the list to prevent it from pulling it again
    del word_count_tally[max_count]

    count += 1

#Clear out the memory of the copied dictionary
del word_count_tally