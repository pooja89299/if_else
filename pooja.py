sex=input("enter m/f")
marriage=input("marriage yes or no")
if sex=="female": 
    if marriage=="yes":
        print("work in urban area")
    else:
        print("she is unmarried")
elif sex=="male":
    age=int(input("enter age"))
    if age>20 and age<40:
        print("work in anywhere")
    elif age>40 and age<60:
        print("work in urban area only")
    else:
        print("error")
else:
    print("nothing")
