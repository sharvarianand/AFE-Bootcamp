# **2)Program to reverse a integer number **

num_2 = int(input("Enter a number: "))
negative = num_2<0
reversed_num = 0
num_2 = abs(num_2) #absolute value is avoid negative nos as below I have kept a condition of positive no while num_2>0: loops can have neg nos.
while num_2>0:
    digit = num_2 % 10
    reversed_num = reversed_num*10 + digit 
    num_2//=10 #Removes the last digit num_2 = num_2//10 (Integer division)
if negative :
    reversed_num = - reversed_num
print("Reversed number =", reversed_num)