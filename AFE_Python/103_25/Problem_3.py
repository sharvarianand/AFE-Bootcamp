# Leetcode Problem 
#Given an array of Integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Brute Force approach though it is to be done with hash map but for now its fine.
Numbers = list(map(int,input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))
Indexes = []   
# Len(Numbers) -  1 is the last index of the list
for i in range(len(Numbers) - 1): #It is going till len of numbers - 2 as last element is not included
    for j in range(i+1,len(Numbers)): #Going till last index i.e. length of numbers - 1
        if Numbers[i] + Numbers[j] == target:
            Indexes.append([i,j])

# print(Indexes if Indexes else "None")
print(f"Indexes = {Indexes}")   

#Using Hash map and 2 pointer approach(Sorted array is required so more complexity) one form left and one from right this are optimal approaches.
# Time complexity is O(n) and space complexity is O(n) in case of hash map approach
