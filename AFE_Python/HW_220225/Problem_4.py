# 4)Calculate the cube of all numbers from 1 to a given number.

num = int(input("Enter a number: "))
if (num<=0):
    print("Please enter a Positive number")
else:
    for i in range(1,num+1):
        print(i**3)
# print(pow(num,3)) #If cube of any number
