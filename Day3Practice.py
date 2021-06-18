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
