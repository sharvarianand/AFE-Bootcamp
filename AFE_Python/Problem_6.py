# check the last digit of given no is divisible by 3 or not 

num = int(input("Enter a number: "))
if num % 10 % 3 == 0:
    print("The last digit of the number is divisible by 3")
else:
    print("The last digit of the number is not divisible by 3")

