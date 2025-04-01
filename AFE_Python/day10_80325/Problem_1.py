# # A sorted list is given and target value is given. 2 sum problem return the indexes which sum upto the target

# nums = list(map(int,input("Enter the numbers: ").split()))
# target = int(input("Enter the target: "))
# indexes = []
# def check_sum():
#     for i in range(len(nums)-1):
#         j=i+1
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 indexes.append([i,j])


# check_sum()            
# print(indexes)            

#Method2(2 pointer approach)
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []

numbers = [2,3,4]
target = 6
two_sum_sorted()
