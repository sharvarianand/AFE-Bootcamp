# Reverse the words not characters
#Ex Sharvari is Learning to code
#Output: code to Learning is Sharvari

# Name = input("Enter the name: ")
# words = Name.split()
# reversed_words = words[::-1]
# print(" ".join(reversed_words)) #This thing we can use to store it in a variable for ex result = the line # Output: code to Learning is Sharvari
# print(*reversed_words) #cannot be stored in a variable directly print

#Sir's method
s = "Sharvari Anand Bhondekar"
lst = s.split()
# rv = (reversed(lst))
# print(rv)
reversed_string = ""
for i in reversed(lst):
    reversed_string += i + " "
# print(reversed_string)    

#How to remove the trailing spaces from a string : strip
reversed_string = reversed_string.strip() #There will be no extra space after last word
print(reversed_string)