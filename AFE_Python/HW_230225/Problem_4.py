#Find the second largest number in list

num = list(map(int,input("Enter the numbers: ").split()))

largest = float('-inf')
second_largest = float('-inf')

for i in num:
    if i> largest:
        second_largest = largest
        largest = i
    else:
        if i >second_largest  and i != largest:
            second_largest = i

print(second_largest)                