# 2 sorted lists to merge in the sorted order
#Merge 2 sorted lists

list_1 = list(map(int,input("Enter the numbers: ").split()))
list_2 = list(map(int,input("Enter the numbers: ").split()))
merged_list = list_1 + list_2
for j in range(len(merged_list)):
    key = merged_list[j]
    i = j - 1
    while i >= 0 and merged_list[i] > key:
        merged_list[i + 1] = merged_list[i]
        i = i - 1
    merged_list[i + 1] = key
print(merged_list)    

#Method 2

list_1 = list(map(int,input("Enter the numbers: ").split()))
list_2 = list(map(int,input("Enter the numbers: ").split()))
merged_list = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i] > list_2[j]:
            merged_list.append(list_2[j])
            list_2.pop(j)
        else:
            merged_list.append(list_1[i])
            list_1.pop(i)
print(merged_list)           



