# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


nums = [2,2,1,1,1,2,2]
n = len(nums)

def majority_element(nums):
    for i in nums:
        count = sum(1 for j in nums if j == i) #Generator Expression
        if count > n//2:
            return i   

print(majority_element(nums))
