a=int(input("enter a value="))
b=int(input("enter b value="))
a=a^b
b=a^b            #swap two numbers
a=a^b
print("now a is:",a)
print("now b is:",b)
print("-----------------")
# convert numbers to binary.....
#volume of sphere
r=float(input("enter r value:"))
volume=(1.3)*(3.14)*r*r*r
print("volume of cone is:",volume)
#volume of cone :1/3 pi r square h
print("---------------------------")
r=float(input("enter r value:"))
h=float(input("enter h value:"))
volume=(0.3)*(3.14)*r*r*h
print("volume of cone is:",volume)
#volume of cylinder is pi r square h
print("-------------------------------")
r=float(input("enter r value:"))             #my code
h=float(input("enter h value:"))
volume=(3.14)*r*r*h
print("volume of cylinder is",volume)
#area of equilateral triangle is root 3/4* a square(a:side)
print("-------------------------------------")
a=float(input("enter a side"))
area=(0.43)*a*a                        #my code
print("area is equilateral triangle is:",area)
print("---------------------------------------------")
#CI
r=float(input("enter intrest rate"))
p=int(input("enter principal amount"))
t=int(input("enter time period"))
ci=p*(1+r)**t
print("compound intrest is:",ci)
print("-.-.-.-.-.-.-.")
#equilateral
a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
s=int(input("enter s value"))
area=s*(s-a)*(s-b)*(s-c)
print(area)
