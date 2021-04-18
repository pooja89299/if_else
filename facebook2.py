print("create facebook account")
language=input("enter the language")
if language=="english" or language=="hindi":
    name=input("enter your name and surname")
    if name=="poojarani":
        email_id=input("enter your email id")
        if email_id=="poojarani@gmail.com":
            password=input("enter password")
            if password==password:
                gender=input("enter the gender")
                if gender=="male" or gender=="female" or gender=="others":
                    print("vaid")
                else:
                    print("invaild")
            else:
                print("invaild")
        else:
            print("invaild")
    else:
        print("invaild")
else:
    print("nothing")
