#Need to rotate a array given number of times

Numbers = list(map(int,input("Enter the numbers: ").split()))
d = int(input("Enter the number of times the array need to rotate: "))

for i in range(d): #one less than given 
    Numbers.insert(0,Numbers.pop())

print(Numbers)        