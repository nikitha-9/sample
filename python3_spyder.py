#if syntax is like : "if condition:"and it doesnt have curly braces
#and it ends when we end indent (space) ::""simple if""
print("simple if")
n=int(input("enter no"))
if(n>100):
    print("this is if block")
    print(n)
print(" this is outer if block as it is simple if")#also prints this as it is simple if
print("------------------if else----------")
#else syntax:no conditions only "statements:"<- syntax
n=int(input("enter no"))
if(n>100):
    print("this is if block")
    n+=1
    print(n)
else:# end indent(space) from if block that means"}"
    print("this is else block")
    n-=1
    print(n)
    print("---------ladder if else---------------")#if. elif.else
n=int(input(" enter n value"))
if(n==0):
    print("zero")
elif(n>0):
    print("+ve")
else:
    print("-ve")
#write a program to calculate given year is leap year or not
year=int(input("enter year"))
if (year%400==0 or ( year%4==0 and year%100!=0)):#keeping 1600 in mind we had that statement
    print(" leap year")
else:
    print("non leap year")
print("task hw -1")
#joy picking a number
n=int(input("hey joy pick a number="))
if(n%2!=0):
    print("weird")
elif(n%2==0 and 2<n<5):
    print("not weird")
elif(n%2==0 and  6<n<20):
    print("weird")
elif n%2==0 and n>20:#joy picked 80 so this has executed
    print("not weird")
print("home work-2")
ch=int(input("teja picked number in a b c d f p v"))
switch (ch)
case 'a':case 'A':
       print("adda language is selected for installation")
       break;
case 'b':case'B':
       print("basic is selected for installation")
       break;
case 'c':case 'C':
       print("cobalt is selected for installation")
       break;
case 'd':case 'D':
       print("dbase is selected for installation")
       break;
case 'f':case 'F':
       print("fortran is selected forv installation")
       break;
case 'p':case'P':
       print("pascal is selected for installation")
       break;
case 'v':case'V':
       print("visual c ++ is selected for installation")
       break;
case_:
       print(" wrong choice")
    
    
    







