# Today is the 16th day of Python Practice
# This is more array problems from leetcode

# 1.
# Given an array arr, replace every element in that array with the greatest element 
# among the elements to its right, and replace the last element with -1.

def replaceElements(arr):

    if len(arr) <= 1:
        return [-1]

    for index in range(len(arr) - 1):
        arr[index] = max(arr[index + 1:])

    arr[len(arr) - 1] = -1

    return arr
    # This is my second try. I did not know about the max() function
    # O(n)


    #if len(arr) <= 1:
    #    return [-1]

    #max_value = 0

    #for index in range(len(arr) - 1):
    #    max_value = arr[index + 1]
    #    for j in range(index + 1, len(arr) - 1):
    #        if max_value < arr[j + 1]:
    #            max_value = arr[j + 1]
    #    print(max_value)
    #    arr[index] = max_value
    #arr[len(arr) - 1] = -1

    #return arr
    # THis is my first try
    # O(n^2)

arr = [17,18,5,4,6,1]
#print(replaceElements(arr))
arr2 = [400]
#print(replaceElements(arr2))

# 2.
# Given an array nums of non-negative integers, return an array consisting 
# of all the even elements of nums, followed by all the odd elements of nums.

def sortArrayByParity(nums):

    evenNums = []
    oddNums = []

    for index in range(len(nums)):
        if (nums[index] % 2) == 0:
            evenNums.append(nums[index])
        elif nums[index] % 2 == 1:
            oddNums.append(nums[index])



    paritySorted = evenNums + oddNums

    return paritySorted

nums = [3,1,2,4]
print(sortArrayByParity(nums))
nums2 = [3,1,2,4]
