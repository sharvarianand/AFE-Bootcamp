#Check if all numbers are prime.

numbers = list(map(int, input("Enter the numbers: ").split()))
prime_numbers = []
all_prime = True

for num in numbers:
    if num < 2:  
        continue  

    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            break  
    else:  
        prime_numbers.append(num)  

print("Prime numbers in the list:", prime_numbers if prime_numbers else "None")

if all_prime and len(prime_numbers) == len(numbers):  
    print("All numbers are prime.")
else:
    print("All numbers are not prime.")

