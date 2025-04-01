# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

s = input("Enter the string: ")
s = s.lower()

def is_Palindrome(s):
    left = 0
    right = len(s) - 1
    while left<=right:
        if s[left] != s[right]:
            return False
        left+=1            
        right-=1
    return True  
        
        
print(is_Palindrome(s))        