
# a =('python',)*5
# print(a)

# tpl = (1,2,3,4,5,6,7,8,9,10)
# # del tpl[0] #Immutale cannot delete a single element but can delete the whole tuple
# # print(tpl)
# # print(len(tpl))
# lst = [1,3,4,5,6]
# tpl = tuple(lst)
# print(tpl)
# t3 = tpl[: : -1 ] #last index is not included it is exclusive
# # t4 = b[2: ]
# print(t3)
# # print(t4)

#Ways to create a tuple

# tpl = (1,2,3,4,5,6,7,8,9,10) 
# tpl2 = 1,2,3,4,5,6,7,8,9,10
# tpl3 = tuple([1,2,3,4,5,6,7,8,9,10])
# tpl4 = ()
# tpl5 =('python',)*5
#Tuple packing 
a,b,c = 10,20,30
tpl = (a,b,c)
print(tpl)


