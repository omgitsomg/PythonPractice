# This is day 3 of my python practice over the summer.
# Today, I will focus on learning about dictionaries


# In my own words, I would say dictionaries in Python are
# similar to linked lists where there are keys and values
# attached to each other.

# The indexes in dictionaries does not have to be an int.
# They could be strings.


# To initialize a dictionary in Python
# The output of the code will be the value of 'Work Phone',
# which is (888) 888-8888
practice_Dictionary = {'Home Phone' : '(999) 999-9999' ,
                       'Work Phone' : '(888) 888-8888' }
empty_dictionary = {}
print(practice_Dictionary['Work Phone'])


# An example showing how to print the keys and value of
# the dictionary
# The output is 
# dict_values(['(111) 111-1111', '(222) 222-2222', '(333) 333-3333', '(444) 444-4444'])
# dict_keys(['Mom', 'Dad', 'Older Brother', 'Kevin Ly'])

phone_numbers = {'Mom' : '(111) 111-1111',
                 'Dad' : '(222) 222-2222',
                 'Older Brother' : '(333) 333-3333',
                 'Kevin Ly' : '(444) 444-4444'}
printPhoneNumbers = phone_numbers.values()
printKeys = phone_numbers.keys()
print(printPhoneNumbers)
print(printKeys)

# Dictionaries can also hold other dictionaries.
# For example

grouped_dictionary = {'random_dictionary' : {1000 : '1',
                                           1001 : '2',
                                           1002 : '3',
                                           1004 : '4'},
                      'name_Dictionary' : {'Student 1' : 'Kevin',
                                         'Student 2' : 'Steven'}}
print(grouped_dictionary['random_dictionary'][1000])

# Small hint. The keys for the Python Dictionary
# cannot contain mutable types like lists and dictionaries.

# Useful operations for Python Dictionaries.
# dict.frommkeys(keys, value)

Family_members = ('Mom', 'Dad', 'Brother', 'Me')
household = dict.fromkeys(Family_members, None)
print(household)

# You can create a dictionary like this.

five_multiplier = {x : x*5 for x in (5, 10, 100)}
print(five_multiplier)

adverb_dictionary = {x : x + "ly" for x in ("careful" , "painful", "beautiful")}
print(adverb_dictionary)

# to overwrite an entry within the dictionary
# simply assign a new value to it. No need to delete it first.

phone_numbers['Mom'] = "(555) 555-5555"
print(phone_numbers["Mom"])

# list() function returns all the keys in insertion order.

listed_familyMem = list(Family_members)
print(listed_familyMem)

# Whilte sorted() function returns the keys in alphabetical order.

alphabetical_familyMem = sorted(Family_members)
print(alphabetical_familyMem)

# How to loop through a Python Dictionary
# The items() function returns an iterable view object.

print(phone_numbers.items())
for family_member, phoneNum in phone_numbers.items():
    print(family_member, "\'s Phone number:", phoneNum)

# In addition, you can merge two dictionaries into one
# For example
# If they are any overlapping keys between the two,
# then the latest key gets chosen with its value

dictionary1 = {'first' : 1,
               'second' : 2,
               'third' : 3}
dictionary2 = {'fourth' : 4,
                'fifth' : 5,
                'sixth' : 6}
dictionary12 = {**dictionary1, **dictionary2}
print(dictionary12)

# The clear() function simply clears the whole dictionary
# including the keys and values

# To get an entry given the key, use the get(key) function





