#binary files
import pickle
str="binary files"
f1=open("nikitha.bin","wb")#can be of any mode
pickle.dump(str,f1)#pickling(serialization)
f1.close()
print("load")
f2=open("nikitha.bin","rb")
lst=pickle.load(f2)#depickling(deserialization)
print(list(lst))
f2.close()
print("java script json ")
import json# related to java script
student={
    "name":"nikitha"
     }
with open("dtp.json","w")as pl:
    json.dump(student,pl)
with open("dtp.json","r")as pl:
    d=json.load(pl)
    print(d)
import csv
fi=open("data1.csv","w")#comma seprerated version(csv)
fn=["hi","world"]
wr=csv.DictWriter(fi,fieldnames=fn)
wr.writeheader()
wr.writerow({"hi":"nikitha","world":"19"})
fi.close()
print("reading csv files")
with open("data1.csv")as file:
    dt=csv.reader(file,delimiter=",")
    for i in dt:
        print(i)


    
    
    
    



