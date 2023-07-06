# from array import *
# ar=array('i',[])
# n=int(input("enter limit"))
# for i in range(n):
#     ele=int(input("enter element"))
#     ar.append(ele)
# print(ar)


# print("list handling in python")
lis=[22,8,9,99,80]
print(lis)
print(len(lis))
#gives length of string
print(sum(lis))
#prints sum of the numbers of a string
print(min(lis))
print(max(lis))
lis.append(888)
lis.append(777)
print(lis)
lis.extend({12,98,81})
print(lis)
lis.insert(700,656)#inserting only one element
print(lis)
lis.remove(80)
print(lis.pop())
print(lis)
lis.reverse()
print(lis)
lis.sort()
print(lis)
del lis[0]#it means that it will delete a value of 0th index
print(lis)
print(lis.count(12))#it counts the number of twelves in the list
print(lis.index(81))
lis.clear()
print(lis)
d={2:4,8:64,7:49,9:81}
print(d)


