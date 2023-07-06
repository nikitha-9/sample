#binomial expansion
#nc0 .a^n.b^0+nc1.a^(n-1).b^1+............ is the series
#where ncr =n!/(n-r)!.r!
#(n-r)!=n(n-1)(n-2)(n-3)==nc4
n=int(input())
coeff=1
for i in range(0,n+1):
    coeff=1
    if(i==0 or i==n):
        coeff=1                     #here we took nci instead of ncr
    elif(i!=0 or i!=n):
            for i in range(1,i+1):
                coeff=(coeff*((n+1)-i)/i)#ncr=(n+1)-r/r
    print(str(int(coeff))+" "+"a^",n-i," "+"b**",i,"+",end=" ")
    

