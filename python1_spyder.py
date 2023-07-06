x=10#assignment operators
y=9
x+=y
print(x,y)#x=x+y
x*=y
print(x,y)
x/=y
print(x,y)
x-=y
print(x,y)
x**=y#x=x**y
print(x,y)
x=5
x+=10
print(x)
x=5#relational operators
y=3
print(x<y)
print(x>y)
print(x==y)
print(x<=y)
print(x>=y)
print(x!=y)
#logical operators: and, or, not
print(x>=y and x!=y)#if both are true its true
print(x==y or x<y)#if both are false it is false
print(not(x!=y))#prints true to false and false to true
#membership operator: in, not in
s="hi i am nik"
print("nik"in s)
print("o "in s)
print("n"in s) 
print("nik" not in s)
#identity operator:is ,is not
x=3
y=3
z=2
print(x is y)
print(x is not y)
print(x is not z)
x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)# in list the default output is false
#as [1,2,3,4] is a list answer gets false
#for tuple it shows correct answer as it is immutable
x=(1,2)
y=(1,2)
print(x is y)
print (x is not y)
#bitwise operators:& | ^ << >> ~
x=2
y=3
print(x&y)#changes 2 and 3 values to binary and perform and(multiplication) operation
print(x|y)# takes binary values of 2 and 3 and performs or operation
print(~x)# its print 2s complement of x
print(x>>1)#x will move one step left
print(x<<2)#x will move 2 steps right as right shift
