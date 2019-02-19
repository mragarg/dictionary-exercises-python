
letters = 'bdfhjlnprtvwza cegikmoqsuwy'
secret = [9, 16, 23, 9, 14, 20, 16, 23, 23, 13, 17, 16] # "test message"

def translate(index, master):
    return master[index]

def map_over_decode(collection, master, how):
    result = ''
    for item in collection:
        result += how(item, master)

    return result

def decode(number_list, master_list):
    return map_over_decode(number_list, master_list, translate)

def decode_while(number_list, master_list):
    # configuration came in as arguments
    result = ''
    count = 0
    max_length = len(number_list)

    # do the translation
    # for each item in number_list...
    # for item in number_list:
    while count < max_length:
        result += master_list[number_list[count]]
        count += 1

    # return the result
    return result

print(decode(secret, letters))
print(decode_while(secret, letters))
print(map_over_decode(secret, letters, translate))

#Work on adding Encoder 
def convert_letters_to_numbers(a_letter, master):
    #find a letter in master
    #save the index
    #return it
    return master.index(a_letter)

def map_over_encode(collection, master, do_translation):
    result = []
    for letter in collection:
        result.append(do_translation(letter, master))
    return result

def encode(message, master):
    return map_over_encode(message, master, convert_letters_to_numbers)

print(encode("test message", letters))
#[13, 22, 3, 17, 22, 3]