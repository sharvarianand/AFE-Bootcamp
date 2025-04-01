# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Brute Force approach
# nums = list(map(int,input("Enter the numbers: ").split()))

# count = 0
# for i in nums:
#     if i == 0:
#         count+=1
#         nums.remove(i)

# nums.extend([0] * count)
# print(nums)    
# Not to use remove as it increases the time complexity

nums = list(map(int,input("Enter the numbers: ").split()))
n = len(nums)

def move_zeroes(nums):
    write_index = 0
    for i in range(n):
        if nums[i] != 0:
            nums[write_index] = nums[i]
            write_index+=1

    for i in range(write_index,n):
        nums[i] = 0
    return nums

print(move_zeroes(nums))     
# Time complexity: O(n)
