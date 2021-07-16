# Today is the 15th day of Python Practice
# I am doing more problems from leetcode about arrays

# 1.
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

def checkIfExist(arr):


    # If there are more than 2 zeros, then return True
    countZeros = 0
    for index in range(len(arr)):
        if arr[index] == 0:
            countZeros += 1

        if countZeros >= 2:
            return True


    # Go through the List, if there are any elements when doubled are equal to
    # one of the other elements, return True
    for index in range(len(arr)):
        if (arr[index] * 2) in arr and arr[index] != 0:
            print(arr[index] * 2)
            return True
    return False

arr = [10,2,5,3]
arr2 = [7,1,14,11]
arr3 = [3,1,7,11]
arr4 = [-2,0,10,-19,4,6,-8]
arr5 = [0,0]
print(checkIfExist(arr))
print(checkIfExist(arr2))
print(checkIfExist(arr3))
print(checkIfExist(arr4))
print(checkIfExist(arr5))

# 2.
# Given an array of integers arr, return true if and only if it is a valid mountain array.

def validMountainArray(arr):

    # if the list is less than 3 elements, return False
    lengthArr = len(arr)
    if lengthArr < 3:
        return False

    max_value_index = 0
    max_value = arr[0];

    # Find the largest value in the list
    for index, items in enumerate(arr):
        if items > max_value:
            max_value = items
            max_value_index = index

    # If the peak of the mountain is at the beginning or end of the list, return False
    if max_value_index == 0 or max_value_index == (lengthArr - 1):
        return False
    

    # Strictly increasing
    for value in range(max_value_index):
        if arr[value] >= arr[value + 1]:
            return False
    
    # Strictly decreasing
    previousVal = max_value
    for value in range(max_value_index + 1, lengthArr):           
        if previousVal <= arr[value]:
            return False
        else:
            previousVal = arr[value]

    return True

#if len(arr)<3 or arr[0]>arr[1]:
#            return False
#        uphill = True
        
#        for i in range(1,len(arr)):
#            if arr[i]==arr[i-1]:
#                return False
            
#            if uphill:
#                if arr[i]<arr[i-1]:
#                    uphill = False
            
#            else:
#                if arr[i]>arr[i-1]:
#                    return False
        
#        return not uphill
# The code in comments is another solution to the problem givem from leetcode.

arr = [2,1]
print(validMountainArray(arr))
arr2 = [3,5,5]
print(validMountainArray(arr2))
arr3 = [0,3,2,1]
print(validMountainArray(arr3))
arr4 = [0,1,2,1,2]
print(validMountainArray(arr4))

