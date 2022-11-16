Num1 = int(input("enter the number"))
Num2 = int(input("enter the number"))
Num3 = int(input("enter the number"))
Num4 = int(input("enter the number"))
 
if(Num1>Num4):
    f1 = Num1
else:
    f1 = Num4

if(Num2>Num3):
    f2 = Num2
else: 
    f2 = Num3

if(f1>f2):
    print(str(f1) + "is the greatest")
else:
    print(str(f2) + "is the greatest")


