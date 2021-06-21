# Hello, this is day 4 of my Python practice.
# Today, I will focus on learing how to iterators
# function within Python and loops, specifically for-loops
# and while-loops.

# for-loops
# Remember to put a colon at the end
# of the for-loop statement
# In addition, an indent is needed to put the statement 
# within the for-loop scope.

# Example 1

string = "STRING"
for letter in string:
    print(letter)

# Example 2

randomList = [1, 2, 3, "one", "two", "three"]
for item in randomList:
    print(item)

# Example 3
# How to get an entry from the list or string
# Simply use the "random_Iterable[index of entry]".

print(randomList[2]) # This will print 3
print(randomList[5]) # This will print "three"

print(string[2]) # This will print "R"
print(string[4]) # This will print "N"

# while-loops
# Similar to Java's while-loop, with some small differences
# Remember the colon at the end of the while statement
# and the indent.

# Example 1

i = 5
while i > 0:
    print(i, end = ' ')
    i = i - 1

print()

# Example 2
# This is will "STRING" in reverse

i = len(string) - 1
while i >= 0:
    print(string[i], end = ' ')
    i = i - 1

print()


# Iterators are objects that can be iterated through until
# there are no more elements to look through.

# Example 1

string1 = "12345"

for number in string1:
    print(number)


# Example 2
# Lists can, also, be iterated through

abcdList = ["A", "B", "C", "D"]
for letter in abcdList:
    print(letter, end = ' ')

print()

# Example 3
# The for-loop is able to print both the keys and
# the values of the dictionary using that form
# for x, y in dictionary.items()
# x = keys, y = values

family_dictionary = {"Mom" : "1",
                     "Dad" : "2",
                     "Brother" : "3",
                     "Myself" : "4"}
for familyMember, number in family_dictionary.items():
    print(familyMember + "\'s Number: " + number)


