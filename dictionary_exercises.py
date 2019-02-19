phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#Print Elizabeth's phone number
def print_entry(dictionary, name):
    return dictionary[name]

#Add an entry to the dictionary (Kareem)(938-489-1234)
def new_entry(dictionary, name, phone):
    dictionary[name] = phone
    return dictionary

#Delete Alice's phone entry
def delete_entry(dictionary, name):
    del dictionary[name]
    return dictionary

#Change Bob's phone number to (968-345-2345)
def change_number(dictionary, name, phone):
    dictionary[name] = phone
    return dictionary

#Print all the phone entries
def print_phone(dictionary):
    for key in dictionary:
        print(dictionary[key])

print_phone(phonebook_dict)