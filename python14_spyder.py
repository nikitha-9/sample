#exception handling
#try
#except
#finally
#raise
dat=[12,6,88,'f']
try:
    sum=0
    for i in dat:
        sum+=i
        print(sum)
except TypeError:    #if except block is not written the console prints "type error",doesnt prints anything
    print("sum of character is not possible")
rrr=[3,4,2,1,7]
try:
    sum=0
    for i in rrr:
        sum+=i
        print(sum)
        print(rrr[10])
except TypeError:
    print("wrong type")
except IndexError:
    print("index is out of rrr range")
finally:
    print("this is finally block")
n=int(input("enter n value"))
try:
    if n<7:
        raise ValueError("less than 7 not accepted")
    else:
        print(n)
except IndexError:
    print("error")
