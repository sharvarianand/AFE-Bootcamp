#Count Pairs Whose Sum is Less Than Target

#Brut Force Approach
# def count_pairs(nums,target):
#     pairs = []
#     count = 0
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] < target :
#                 pairs.append((nums[i], nums[j]))
#                 count+=1            
#     return pairs, count

# Numbers = list(map(int,input("Enter the numbers: ").split()))
# target = int(input("Enter the target: "))
# pairs, pairs_count = count_pairs(Numbers, target)
# print(f"Valid Pairs: {pairs}")
# print(f"Number of pairs whose sum is less than {target} are: {pairs_count}")

#Optimized Aproach
def count_pairs(nums, target):
    nums.sort()
    count = 0
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] < target:
            count += (right - left)  # All elements between left and right are valid
            left += 1
        else:
            right -= 1
    return count

nums = list(map(int, input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))
pairs_count = count_pairs(nums, target)
print(f"Total number of pairs having sum less than target = {pairs_count}")
