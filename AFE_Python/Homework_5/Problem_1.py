#Remove duplicates from an array

# Numbers = list(map(int,input("Enter the numbers: ").split()))

# Numbers = list(dict.fromkeys(Numbers))
# print(Numbers)


#Most optimized Approach
# def remove_duplicates(nums):
#     seen = set() # Seen is a set used so we dont have to iterate through the list to check if the number is already present
#     unique_Numbers = [] # List to store the unique numbers
#     for num in nums:
#         if num not in seen:
#             seen.add(num)      
#             unique_Numbers.append(num)
#     return unique_Numbers   #Function should always have a return value otherwise none will be returned that also on first for loop.

# Numbers = list(map(int,input("Enter the numbers: ").split()))
# Numbers = remove_duplicates(Numbers)
# print(Numbers) # We can do even print(remove_duplicates(Numbers))

def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k

nums = list(map(int, input("Enter the sorted array of numbers: ").split()))
print("Original array:", nums)
k = removeDuplicates(nums)
print("Number of unique elements:", k)
print("Modified array:", nums[:k])


