# Search a element in the list

Numbers = []
n = int(input("Enter a number of Elements: "))
for i in range(n):
    Element = int(input("Enter a Number: "))
    Numbers.append(Element)
Target = int(input("Enter the target element: "))
for i in range(len(Numbers)):
    if(Numbers[i] == Target):
        print(i)
        break
else:
    print("-1")        