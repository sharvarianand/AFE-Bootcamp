#Count frequency of list elements

numbers = list(map(int, input("Enter the numbers: ").split()))
unique_numbers = [] 
frequency = []  

for num in numbers:
    if num in unique_numbers:
        index = unique_numbers.index(num)  
        frequency[index] += 1  
    else:
        unique_numbers.append(num) 
        frequency.append(1) 

for i in range(len(unique_numbers)):
    print(f"{unique_numbers[i]} appears {frequency[i]} times")

