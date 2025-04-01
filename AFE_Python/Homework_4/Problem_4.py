# # Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

#Brut Force Approach 
def sum_of_squares(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit ** 2
        n //= 10
    return sum

def happy_no(n):
    for _ in range(100):  
        n = sum_of_squares(n)
        if n == 1:
            return True  
    return False  

num = int(input("Enter the number: "))
print(happy_no(num))


# def sum_of_squares(n):
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum+= digit ** 2
#         n //= 10
#     return sum 

# def happy_no(n):
#     for _ in range(100):
#         n = sum_of_squares(n)  #For removing infinite loops we r running it for arbitary 100 times.
#         if n == 1:
#             return True
#     return False