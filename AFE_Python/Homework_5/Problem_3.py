def countFairPairs(nums, lower, upper):
    nums.sort()
    n = len(nums)
    count = 0

    for i in range(n):
        left = i + 1
        right = n - 1
        lower_bound = lower - nums[i]
        upper_bound = upper - nums[i]

        low = left
        high = right
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < lower_bound:
                low = mid + 1
            else:
                high = mid - 1
        start = low

        low = left
        high = right
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > upper_bound:
                high = mid - 1
            else:
                low = mid + 1
        end = high

        if start <= end:
            count += end - start + 1

    return count

nums = list(map(int, input("Enter the list of numbers: ").split()))
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print("Number of fair pairs:", countFairPairs(nums, lower, upper))
