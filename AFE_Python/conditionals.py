#conditionals
# #if
age = 20
# if age >= 18:
#     print("You are eligible to vote.")
# #short hand property
# if age>=18 : print("You are eligible to vote.")

#if-else(Short hand property for elif)
print("you can travel for free") if age>=12 else print("you have to pay")

#nested if else
age = 70
is_member = True 
if age>=60:
    if is_member:
        print("30% discount")
    else:
        print("20% discount")
else:
    print("You are not eligible for discount")        

#Ternary
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

#nested if else in ternary
age = 70
is_member = True
s = "30% discount" if age>=60 and is_member else "20% discount"
print(s)

#6. Match case
number = 2
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
        