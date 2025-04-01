#Leetcode Question
#Remove duplicates from a list 

Numbers = list(map(int,input("Enter the numbers: ").split()))
# Numbers = sorted
# print(Numbers)
Unique_Numbers = []
#For both sorted and unsorted lists
for i in range(len(Numbers)):
    if Numbers[i] not in Unique_Numbers:
        Unique_Numbers.append(Numbers[i])
print(Unique_Numbers)  
         
#Method 1
Numbers = list(map(int,input("Enter the numbers: ").split()))
Numbers = list(dict.fromkeys(Numbers))
print(Numbers)

#Method 2
Numbers = list(map(int,input("Enter the numbers: ").split()))
Numbers = list(set(Numbers))
print(Numbers)

#For sorted list 
a = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,8,8,8,8,8,8]
n = len(a)
if n<=1:
    print(a)

j = 1
for i in range(1,n):
    if a[i] != a[i-1]:
        a[j] = a[i] 
        j=j+1

for i in range(0,j):
    print(a[i])            