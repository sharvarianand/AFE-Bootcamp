# s = input("Enter a string: ")  # Take input
# rev = ""  # Variable to store reversed string

# # Loop through the string in reverse order
# for char in s:
#     rev = char + rev  # Prepend each character to rev

# print("Reversed string:", rev)

num_2 = int(input("Enter a number: "))  # Take input
reversed_num = 0  # Variable to store the reversed number

while num_2 > 0:
    digit = num_2 % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Append it to reversed number
    num_2 //=10  # Remove the last digit //num_2 = num_2//10

print("Reversed number:", reversed_num)
