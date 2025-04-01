# Write a function to check whether the number is prime or not 

def check_prime():
    num = int(input("Enter a number: "))
    if num <=1:
        print("Neither prime not composite")
    else:
        for i in range (2,num):
            if num % 2 == 0:
                print("Not a prime number")
                break
        else:
            print(f"{num} is a prime number")

check_prime()
