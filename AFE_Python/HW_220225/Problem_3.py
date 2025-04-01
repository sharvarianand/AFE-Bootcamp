# 3)Print elements from a given list present at odd index positions.

Names = [ "Aparna","Sharvari", "Pawan", "Omm", "Shruti", "James", "Sumit"]
for i in range(len(Names)):
    if i%2 != 0:
        print(Names[i])
print(Names[1::2]) #List slicing #We want odd index therefore starting from 1
