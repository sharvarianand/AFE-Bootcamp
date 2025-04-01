# 1)Find the factorial of a given number

num_1 = int(input("Enter a number: "))

fact = 1
if(num_1<0):
    print("Please enter a Positive number.")
elif(num_1 == 0):
    print(f"Factorial of {num_1} is 1")   
else:
    for i in range(1, num_1 + 1):
        fact *= i
    print(f"The factorial of {num_1} is {fact}") 