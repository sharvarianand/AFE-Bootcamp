# Remove all the occurences of val in nums and return the number of elements in nums.

nums = list(map(int,input("Enter the numbers: ").split()))
val = int(input("Enter the Target Element: "))

k = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k+=1

print(nums[ : k])
print(k)     
