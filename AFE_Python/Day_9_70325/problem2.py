# Program for Armstrong number

# def check_Armstrong():
#     num = int(input("Enter a number: "))
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#     if num == sum:
#         print(f"{num} is an Armstrong number")
#     else:
#         print(f"{num} is not an Armstrong number")

# check_Armstrong()


def check_Armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp >0 :
        digit = (temp % 10)
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(f"{num} is an Armstrong number.")  
    else:
        print(f"{num} is not an Armstrong number")

check_Armstrong()              


    