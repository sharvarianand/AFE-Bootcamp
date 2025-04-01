# Average of the nos in a list

Numbers = []
n = int(input("Enter a number of Elements: "))
for i in range(n):
    Element = int(input("Enter a Number: "))
    Numbers.append(Element)
sum = 0 
for i in Numbers:
    sum += i
Average = sum/n     
print(f"The average of all the numbers in the list is {Average}")