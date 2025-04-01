#Given an array nums containg n distinct numbers numbers in the range [0,n], return the only number in the range that is missing from the array.


def missingnumber(nums):
    sum=0
    n=len(nums)
    ans=n*(n+1)//2
    for num in nums:
        sum=sum+num
    return (ans-sum)
nums=[0,1,2,4]

print(missingnumber(nums))
