# Today is the 14th day of Python practice.
# This is me continuing my recap and reinforcement of my knowledge in Python.
# Today, I will focus on solving problems from the website leetcode.com.


# 1.
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

def removeElement(nums, val):

    # nums = [x for x in nums if x != val]
    # This is a list comprehension
    # the first 'x' will be returned to nums if that x in nums is not equal to the value given

    count = 0
    lengthNums = len(nums)

    while val in nums:
        count += 1
        nums.remove(val)
        


    return lengthNums - count


# 2.
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

def removeDuplicates(nums):

    lengthNums = len(nums)
    countUnique = 0
    countOriginal = 1

    if lengthNums == 0:
            return 0
    elif lengthNums == 1:
            return 1

    while countOriginal < lengthNums:
        if nums[countOriginal] != nums[countUnique]:
            countUnique += 1
            nums[countUnique] = nums[countOriginal]
            
        countOriginal += 1
            

    return nums

nums = [3,2,2,3]
nums1 = [0,1,2,2,3,0,4,2]
print(removeElement(nums, 3))
print(removeElement(nums1, 2))

nums2 = [1,1,2]
nums3 = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums2))
print(removeDuplicates(nums3))

