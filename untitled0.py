#w a p to read a mobile number as wordds of string and convert that into number string
phonenum=(input("enter ur mobile number:"))
i=phonenum.split()
for x in i:
    if (x=="zero"):
        print("0",end=" ")
    elif x=="one":
        print("1",end=" ")
    elif x=="two":
        print("2",end=" ")
    elif x=="three":
        print("3",end=" ")
    elif x=="four":
        print("4",end=" ")
    elif x=="five":
        print("5",end=" ")
    elif x=="six":
        print("6",end=" ")
    elif x=="seven":
        print("7",end=" ")
    elif x=="eight":
        print("8",end=" ")
    elif x=="nine":
        print("9",end=" ")
print(x)
        


