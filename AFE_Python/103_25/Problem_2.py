# FANG Level Question
# List of Integers is given and target element return a list of index of target element.

Numbers = list(map(int,input("Enter the Numbers: ").split()))
target = int(input("Enter the target element: "))

target_Index = []

for i in range(len(Numbers)): #i is an index
    if Numbers[i] == target:   #Numbers[i] = value to be to be searched
        target_Index.append(i)  
        

if target_Index:
    print(target_Index)
else:
    print(-1)    