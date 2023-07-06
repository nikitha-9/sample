#x,y,z=[int(i) for i in (input("enter numbers")).split(",")]
#print(x+y+z)
#lamda expression or anonymous functions-> a function without any name i.e def not needed,,lamda is a keyword we use here
var=lambda r:3.14*r**2#lambda is the keyword must use
print("area=",var(3))
d=lambda s:s.upper()[::-1]
print(d("nikitha"))
#diff b/w lambda and normal function
#supports single line statement which returns some satement,good for performing short operation and data manipulation  
#normal functions:supports n number of lines but b/w function block only,,good for any cases that contains multiple line requirments
#easy readability(normal function);
value=[lambda a=x:a*10 for x in range (1,5)]
for i in value:
    print(i())

    
    
