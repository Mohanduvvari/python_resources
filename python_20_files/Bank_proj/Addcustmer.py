import pickle
import sys
sys.path.append("D:\\python_resource\\python_resources\\python_20_files\\Emp_project\\Exceptions")
from empexceptions import *
from NameValidation import validate

def addcust():
    with open("customer.data","ab") as fp:
        while True:
            try:
                custno=int(input("\tEnter Customer A/c No:"))
                name=input("\tEnter customer name:")
                custname=validate(name)
                bal=float(input("\tEnter Balance:"))
                pin=int(input("\tEnter customer PIN:"))
                lst=list()
                lst.append(custno)
                lst.append(custname)
                lst.append(bal)
                lst.append(pin)

                pickle.dump(lst,fp)
                print("-"*50)
                print("\tCustomer data saved successfully")
                ch=input("\tDo you have another customer to add (yes/no)")
                if ch.lower()=="no":
                    break
            except ValueError:
                print("\tPlease check you Entered Value - again")
            except SpaceError:
                print("\tDont Enter Space - try again")
            except ZeroNameLengthError:
                print("\tPlease Enter Name")
            except InvalidNameError:
                print("\tName is invalid")

