# #Table of 19
# for i in range(1,11):
#     print(f"19 X {i} = {19*i}")
# i=1
# while i<=10:
#     print(19*i)
#     i+=1

#Problem_12 : Calculate sum of all nos from 1 to 50
# sum = 0
# for i in range(1,51):
#     sum+=i
# print(f"Sum of 1 to 50 numbers = {sum}")  

#  calculate the no is prime or not 

# # Write a program to find whether a given number is prime or not.

# n = int (input("Enter a number: "))
# if(n<=1):
#     print(f"{n} is neither prime nor composite.")
# else:
#     for i in range(2,int(n**0.5)+1):   # instead of n-1 i.e. here upto n we have taken root of n bcz the factors repeat after root of n for ex 4*5=20 5*5=25 5*4=20 therefore it increases efficiecy time complexity specially for bigger nos
#         if(n%i)==0:
#             print(f"{n} is not a prime number.")
#             break
#     else:  # Here not if-else and for else as if n is not divisible by any no everytime not prime will be printed therefore for else
#         print(f"{n} is a prime number.")  



n = int(input("Enter a number: "))
if (n<=1):
    print(f"{n} is neither a prime nor a composite number.")
else:
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")

        