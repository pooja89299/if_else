num=int(input("enter the number"))
if num%4==0:
    if num%100==0:
        if num%400==0:
            print("it is leap year")
        else:
            print("it is not leap year")
    else:
        print("yes it is leap")
else:
    print("it is no leap year")


    
