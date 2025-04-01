# Valid Palindrome_2
# Return true if after removing atmost 1 character from the string , it becomes a palindrome.

# string = input("Enter a string: ")

# for i in string:
#     for j in range(len(string),i,-1):
#         if string[i] == string[j]:
#             count +=1
#     if count == 1 and i != (i+j)/2:
#         string.pop(i)

# print(string)        
               
#Sir's Method

def valid_palindrome(str):
    left =0
    right = len(str)-1
    while left < right:
        if str[left] != str[right]:
            return is_Palindrome(str, left+1,right) or is_Palindrome(str,left,right-1)
        left +=1
        right -=1
def is_Palindrome(str,left,right):
    while left<right:
        if str[left] != str[right]:
            return False
        left +=1
        right -=1
    return True
    
str = "abca"
print(valid_palindrome(str))        
