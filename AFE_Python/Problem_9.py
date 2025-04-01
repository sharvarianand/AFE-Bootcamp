num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if (num_1 > num_2 and num_3):
    print(f"{num_1} is greatest.")
elif(num_2 > num_1 and num_3):
    print(f"{num_2} is greatest.")
else:
    print(f"{num_3} is greatest.")        

