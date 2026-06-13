#empAdd.py #module

import pickle
import  sys


sys.path.append("D:\\python_resource\\python_resources\\python_20_files\\emp_project\\Exceptions")
from NameValidation import validate
from empexceptions import *
def addemp():
    with open("D:\\python_resource\\python_resources\\python_20_files\\Emp_project\\empfiles\\emp.data","ab") as fp:
        while True:
            try:
                print("-"*50)
                empno=int(input("\tEnter Employee Number:"))
                name=input("\tEnter Employee Name:")
                empname=validate(name)
                empsal=float(input("\tEnter Employee salary:"))
                comp=input("\tEnter Employee Company:")
                empcomp=validate(comp)
                print("_"*50)
                lst=list() #creating empty list for adding employee values
                #append emp values to lst obj
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                lst.append(empcomp)

                #save the iterable obj content to the file
                pickle.dump(lst,fp)
                print("\tEmployee Data saved successfully")
                print("-"*50)
                ch=input("\tDo you want to add another employee details (yes/no)")
                if ch.lower()=="no":
                    break
                print("-"*50)
            except SpaceError:
                print("\tDon't Enter Space for your name - Try again")
            except ValueError:
                print("\tPlease check you enter format,str")
            except ZeroNameLengthError:
                print("\tEnter your name - try again")
            except InvalidNameError:
                print("\tIInvalid Name-you-entering ")
