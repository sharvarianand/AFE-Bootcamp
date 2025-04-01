# Count Number of Pairs with Absolute Difference K
def countPairs(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(nums[i] - nums[j]) == k:
                count += 1
    return count

nums = list(map(int, input("Enter the array of numbers: ").split()))
k = int(input("Enter the value of k: "))
result = countPairs(nums, k)
print(f"Number of pairs with absolute difference {k} is: {result}")