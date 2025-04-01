#Sum of all nos in a list
Numbers = []
n = int(input("Enter a number of Elements: "))
for i in range(n):
    Element = int(input("Enter a Number: "))
    Numbers.append(Element)

print(Numbers)
sum = 0 
for i in Numbers:
    sum += i
print(f"The sum of all the nos in the list is {sum}")    