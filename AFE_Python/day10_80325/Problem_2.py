# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
nums = [2,2,1,1,3,3,4,4,5,5,6]

def present_single():
    for i in range (len(nums)):
        j =i+1
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                continue
    else:
        print(nums[i])

present_single()  

#Sirs Method:
def singleNumber(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count+=1
        if count == 1:
            return nums[i]

nums = [2,2,1]
print(singleNumber(nums))                