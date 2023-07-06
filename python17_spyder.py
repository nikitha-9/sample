#write a program to reverse contents of a file using oop class(h/w)
class fl:
    def rev(self):
        f1=open("pa1.txt","r")
        stri=f1.read()
        rs=stri[::-1]
        print(rs)
        f1.close()
obj=fl()
obj.rev()

        
        
        
    