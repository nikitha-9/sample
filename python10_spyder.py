v=lambda l,b,h:l*b*h
print("area is::",v(1,6,7))

varia=[lambda f= n:f *5 for n in range(1,5)]
for i in varia:
    print(i())
var=[lambda a=x :a*10 for x in range(1,5)]
for i in var:
    print(i())
print("------- if else with lambda-------------")
m=lambda o:"evenno"if (o%2==0) else "odd number"
print(m(111))
print("-----------filter function using lambda---------")
li=[8,90,7,86,88,77,75,73]
lst=filter(lambda t:(t%2==0),li)
print(list(lst))#list is a datastructure which we are converting the above filtered li
print("mapping 1----------")
vp=[1,45,67,78,77,76,75,99]
vap=map(lambda b:(b%2==0),vp)#returns boolean type o/p checks whether 1,2,......is even or not ,if evan prints yes
print(list(vap))
print("mapping 2-----------------")
mr=[6,7,1,2]
miss=map(lambda h:(h*2),mr)
print(tuple(miss))
print("-----------filter usage in normal functions---------")
def data(j):
    val=['a','e','i','o','u']
    if (j in val):
        return True     #true,false 1st char shld be cap
    else:
        return False
dt=['j','o','a','k']
ltt=filter(data,dt)
for i in ltt:
    print(i,end=" ")
print("--------mapping 3 addition using sets-----------")
a1=[7,6,5,77,8]
a2=[9,7,77]
lit=map(lambda i1,i2:i1+i2,a1,a2)
print(list(lit),end=" ")
            
    
        