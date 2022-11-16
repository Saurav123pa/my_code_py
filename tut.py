n = int(input())
if(n%2)!=0:
    print("Weird")
elif(n%2 and n>20)==0:
    print("Not Weird")
for i in range(2,5):
        if n%2==0:
            print("Not Weird")
        else:
            for i in range(6,20):
                if n%2!=0:
                    print("weird")