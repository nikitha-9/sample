#binomial sequence h/w
#*
#**
#***
#****
#*****
for i in range(1,6):
    for i in range(1,i+1):
        print("*",end=" ")
    print()
print("functions")
def data(n):#defining a function step 1
    while(n!=0):
        print(n)
        n-=1
data(10)#function calling(2)
data(5)
print("functions1")
def student(id,name):#actual arg id,name
    print("id={} and name={}".format(id,name))
i=101#formal arg i,n
n="manu"
student(i,n)#no of actual args should be call here with same no
def student(id,name,college="iit"):
    print("id={} and name={} and college={}".format(id,name,college))
student(101,"arun")#as no college name given iit sets default as above definination
student(209,"kia","nit")
student(name="nia",id=8)#using keyword also we can call function
#print n number of values irrespective of actual=formal arguments equality prooving
def student(*n):
    print(n)
student(1,2,4,9,0,7,99,88)#no need to see the count if it matches with actual parameters or not
print("keyword lenght")
def student(**n):#keyword lenght
    print(n)
student(id=456,name="nik")
#write a program to reverse each word of a string and replace every letter o with a
#write a program to read list of strings and find largest string within list h/w



    