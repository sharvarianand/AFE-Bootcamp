#Find the largest element in the list 

Numbers = list(map(int,input("Enter the numbers: ").split()))

largest = Numbers[0] #instead of Numbers[0] we can use max(Numbers) or largest = '-infi' too

for num in Numbers:
    if num > largest:
        largest = num 

print(f"Largest number in the list is {largest}")

print(sorted(Numbers))


#Approach 1 - Loops and this code 
#Time complexity: O(n) where n is the number of elements in the list
#Space complexity: O(n) where n is the number of elements in the list 
#Approach 2 - Built-in functions and this code
#Time complexity: O(n log n) where n is the number of elements in the list
#Approach 3 - To sort the array and print the last element.
#Time complexity: O(n log n) where n is the number of elements in the list
#O(n) is better than O(n log n)
# Approach 1 is better than Approach 2 and 3.
