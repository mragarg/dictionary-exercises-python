ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#Function that gets the email address of Ramit
def get_characteristic(dictionary, characteristic):
    return dictionary[characteristic]

#Function that returns the first of Ramit's interest
def get_interest(dictionary, section, number):
    result = []
    for i in dictionary[section]:
        result.append(i)
    return result[number]

#Function that gets the email address of Jasmine
def get_friend_characteristic(dictionary, friend, characteristic):
    for i in dictionary["friends"]:
        if(friend == i["name"]):
            return i[characteristic]

# print(ramit["friends"][0]["email"])

#Function that gets the second of Jan's two interests
def get_friend_interest(dictionary, friend, characteristic, number):
    for i in dictionary["friends"]:
        if(friend == i["name"]):
            return i[characteristic][number]


print(get_friend_interest(ramit, "Jan", "interests", 1))