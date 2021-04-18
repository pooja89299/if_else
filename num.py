a=int(input("eanter the fisrt number"))
b=int(input("enter the sicond number"))
c=int(input("enter the third number"))
if a>b>c:
    print(a,b,"greater number")
elif c>b>a:
    print(c,b,"greater number")
elif b>c>a:
    print(b,c,"greater number")
elif a>c>b:
    print(a,c,"greater number")
elif c>a>b:
    print(c,a,"greater number")
elif b>a>c:
    print(b,a,"greater number")
elif c>a>b:
    print(c,a,"greater number")
elif b>a>c:
    print(b,a,"greater number")
else:
    print("all number are equal")