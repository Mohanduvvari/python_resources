#icici.py if filename/modulename in Bank_package

bname='ICICI'
address='Vishakapatnam'
def simpint():
    p=float(input("Enter your principle amount:"))
    t=float(input("Enter your time period:"))
    r=float(input("Enter your rate of interest:"))
    si=(p*t*r)/100
    totalamt=p+si
    print("-"*50)
    print("\tyour principle amount: ",p)
    print("\tSimple intrest is: ",si)
    print("Your total amount: ",totalamt)
