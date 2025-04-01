# Given an integer array nums, return the most frequent even element.
# If there is a tie, return the smallest one. If there is no such element, return -1.


# def mostFrequentEven(nums):
#     even_nums = [num for num in nums if num % 2 == 0]  
#     if not even_nums:
#         return -1  
    
#     max_count = 0
#     result = float('inf')  

#     for num in even_nums:
#         count = sum(1 for j in even_nums if j == num)  
#         if count > max_count or (count == max_count and num < result):
#             max_count = count
#             result = num

#     return result


# nums = [4, 4, 2, 2, 3, 3, 2, 4, 6, 6, 6, 6]
# print(mostFrequentEven(nums))  

def mostfrequenteven():
    Even_nums = [num for num in nums if num % 2 == 0]
    if not Even_nums:
        return -1
    
    max_count = 0
    result = float('inf')

    for num in Even_nums:
        count = sum(1 for j in Even_nums if j == num)
        if count > max_count or count == max_count and num < result :
            max_count = count
            result = num
    return result        

nums = [4, 4, 2, 2, 3, 3, 2, 4, 6, 6, 6, 6]
print(mostfrequenteven())  