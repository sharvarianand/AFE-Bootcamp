#Remove Duplicates from List

#Using while Loop
Numbers  = list(map(int,input("Enter the numbers: ").split()))
i = 0
while i <len(Numbers):
    j = i+1
    while j < len(Numbers):
        if Numbers[i] == Numbers[j]:
            Numbers.pop(j)
        else:
            j += 1
    i+=1

print(f"List after removal of duplicates: {Numbers}")


#Using Dictionary
Numbers = list(map(int, input("Enter the numbers: ").split()))
Numbers = list(dict.fromkeys(Numbers))  # O(n) time complexity
print(f"List after removing Duplicates: {Numbers}")
