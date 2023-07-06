#file handling:
# how to manipulate data of files
#read:r:read() <--- function
#write(),open()
f1=open("satvika.py","w")
f1.write("hai")
print("file created")
f1.close()
#w a p to count number of character ,lines and spaces within a file
#w a p to copy the data of one file and paste into another file
# w a p to merge data of two files
with open("python12_spyder.py","r")as file:
    tr=file.read()
    print(tr)  #prints whole code of this file
    file.close()
print("copying one file contents 2 others")
fl1=open("python12_spyder.py","r") 
str=fl1.read()
fl2=open("satvika.py","w")
fl2.write(str)
fl1.close()
fl2.close() #whole page of python12 is copied to satvika.py(check in file explorer)
print("program to count no of char spaces and lines")
fi1=open("python12_spyder.py","r")
str=fi1.read()
nol=1 #no of lines
noc=0 #no of char
nos=0 #no of spaces
for i in str:
    noc+=1
    if i=="\n":
        nol+=1
    if i==" ":
        nos+=1
print(nol,noc,nos)  #printed no of lines,char,spaces in this file
fi1.close()
print("merging 2 files")
fil1=open("python12_spyder.py","r")
stri1=fil1.read()
fil2=open("satvika.py","r")
stri2=fil2.read()
fil3=open("new.py","w")
fil3.write(stri1,stri2)
fil1.close()
fil2.close()
fil3.close()




    
#file handling:
# how to manipulate data of files
#read:r:read() <--- function
#write(),open()
f1=open("satvika.py","w")
f1.write("hai")
print("file created")
f1.close()
#w a p to count number of character ,lines and spaces within a file
#w a p to copy the data of one file and paste into another file
# w a p to merge data of two files
with open("python12_spyder.py","r")as file:
    tr=file.read()
    print(tr)  #prints whole code of this file
    file.close()
print("copying one file contents 2 others")
fl1=open("python12_spyder.py","r") 
str=fl1.read()
fl2=open("satvika.py","w")
fl2.write(str)
fl1.close()
fl2.close() #whole page of python12 is copied to satvika.py(check in file explorer)
fi1=open("python12_spyder.py","r")
str=fi1.read()
nol=1 #no of lines
noc=0 #no of char
nos=0 #no of spaces
for i in str:
    noc+=1
    if i=="\n":
        nol+=1
    if i==" ":
        nos+=1
print(nol,noc,nos)
fi1.close()
    
