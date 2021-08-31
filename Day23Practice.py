# Today is the the 23rd day of Python Practice.
# Today, I will try to solve Leetcode problems in Python.

# Q1.
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def merge(nums1, m, nums2, n):


    j = 0
    for index in range(m, len(nums1)):
        nums1[index] = nums2[j]
        j += 1

    nums1.sort()
    print(nums1)

list1 = [-1,0,0,3,3,3,0,0,0]
list2 = [1,2,2]
merge(list1, 6, list2, 3)

#def merge(self, nums1, m, nums2, n):
#        nums1[m:] = nums2[:n]
#        nums1.sort()
# This is one of many solutions to the problem. I preferably like this solution because it is simple to understand and efficient.


    
