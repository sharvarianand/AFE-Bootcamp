# Leetcode Problem 
#Given an array of Integers nums and an integer target, return indices of the three numbers such that they add up to target.

Numbers = list(map(int,input("Enter the numbers: ").split()))
target = int(input("Enter the target: "))
Indexes = []
for i in range(len(Numbers)-2): #It is going till len of numbers - 2 as last element is not included
    for j in range(i+1,len(Numbers)-1):
        for k in range(j+1, len(Numbers)): 
            if Numbers[i] + Numbers[j] + Numbers[k] == target:
                Indexes.append([i,j,k])

# print(Indexes if Indexes else "None")
print(f"Indexes = {Indexes}")   