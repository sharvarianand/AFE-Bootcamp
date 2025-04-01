# 5)Find the sum of the series up to n terms  

num_3 = int(input("Enter a number: "))
summation = 0
for i in range(1, num_3+1):
    summation = (num_3 * (num_3 + 1)) // 2 #formula and execution time will be reduced
print(f"The sum of the series up to {num_3} terms is {summation}")
