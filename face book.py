print("create facebook account")
name=input("enter the fist name")
if name>"a" and name<"z":
    surname=input("enter the surname")
    if surname>"a" and surname<"z":
        id=input("enter the your email address or phone number")
        if id>"a" and id<"Z" or id<"9" or id=="@":
           passward=input("enter the passward")
           if passward>"a" and passward<"z" or passward<"9" or passward=="@#$&%":
                print("this is strong password",passward)
                date=int(input("enter the your date of birth"))
                if date =0<"9":
                    gender=input("enter the gende")
                    if gende=="female" or gende=="male":
                        print("your account successful")
                    else:
                        print("not create account")
                else:
                    print("your date of b birth is not difind")        
            else:
                print("its is not strong password")        
        else:
            print("your id is not dirfind")
    










