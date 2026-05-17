#here we are creating business logic for the exceptions
#thi is also a module
from python_19_errors_exceptions.multiplicationtables.multiplication_tables_exceptions import *
def table(n):
    if n.isspace():
        raise SpaceError
    else:
        num=int(n) #possible of raise ValueError
        if num==0:
            raise ZeroError
        elif num<0:
            raise NegativeNumError
        else:
            print("-"*50)
            print("multiplication for {}".format(num))
            print("_"*50)
            for i in range(1,11):
                print(f"{num}*{i}={num*i}")
            print("_"*50)