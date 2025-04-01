print("*****")
print("   *")
print("  *")  
print(" *")
print("*****")

print("*****\n   *\n  *\n *\n*****")

n = 5  # Size of the 'Z'
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == n - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


a,b,c = 10,20,30
print(a,b,c)    

x,y,z = "Hello WOrld"
print(x,y,z)