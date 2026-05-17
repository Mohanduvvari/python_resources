#icici.py  filename/modulename
bname='icici'
address='vishakapatnam'
def simpint():
    p=float(input("Give principle amount:"))
    t=float(input("Enter time period:"))
    r=float(input("Enter rate of intrest:"))
    si=(p*t*r)/100
    totalamout=p+si
    print("simple intrest calaculations")
    print("-"*50)
    print("principal amount=",p)
    print("time period=",t)
    print("rate of intrest=",r)
    print("-"*50)
    print("\tintrest=",si)
    print("\ttotal amount=",totalamout)
    