#Get smallest number in the List
Numbers = list(map(int,input("Enter the numbers: ").split())) #Map throws error if input not given or invalid input therefore no condition required for empty list or invalid input
print(f"Numbers = {Numbers}")

smallest_number = Numbers[0]
for num in Numbers:
    if num < smallest_number:
        smallest_number = num

print(f"Smallest number = {smallest_number}") 