

#1.w a  py prog to read a string as password it must b 8 digits
   # atleast 1 digit should b there
    #first char should b upper case
    #if password is crct else incrct:
#2. w a p to read a mob ile no as words of string and convert that to n umeric string
password=str(input("enter ur password="))
cap_str="QWERTYUIOPSDFGHJKLZXCVBNM"
one_str="1234567890"
a=0
if(len(password)>=8):
    if(password[0] in cap_str):
        for x in range(1,(len(password)+1)):
            if (password[x] in one_str):
                a=1
            
if a==1:
    print("password is incrct")
elif(a==0):
    print("password is crct")
              
                                


                  
    
         
      
    

        
    
        
        



    


    
        

        

        
        
    
    
      
