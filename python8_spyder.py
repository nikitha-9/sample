#
#def data(n):
  #  sum=0
#  while n!=0:
#        sum+=n
 #       n-=1
  #      return sum# it can also returns many variables at a time if we do that it returns tuple 
#print(data(15))
#recursive function similar to loop ,instead of loop we use that
#def data(n):
#    if n>=0:
 #       print(n)
 #       return data(n-1)
#data(10)#instead if we use print(data(10))it prints none at last

#def fact(n):
#    if(n>0):
#        return n*fact(n-1)
#    else:
#        return 1
#print(fact(5))
#w a program to print sum of individual numbers using recursive functions
def data(num):
    a=num%10
    b=num//10
    c=num//100
    r=a+b+c
    return r

print(data(123))#that means it jumps to 23 line and execution starts over there,recursive function executions starts faster



        
    



    

