#Remove even nos from List.
Numbers = list(map(int, input("Enter the numbers: ").split()))
i = 0
while i < len(Numbers):
    if Numbers[i] % 2 == 0:
        Numbers.pop(i)  
    else:
        i += 1  
print(Numbers)

# Numbers = list(map(int, input("Enter the numbers: ").split()))
# Numbers = [i for i in Numbers if i % 2 != 0]  # Keep only odd numbers
# print(Numbers)
