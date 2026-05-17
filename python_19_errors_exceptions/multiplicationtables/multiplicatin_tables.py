#this is main program by which we can write/trigger exception
from python_19_errors_exceptions.multiplicationtables.multiplication_tables_exceptions import *
from python_19_errors_exceptions.multiplicationtables.multiplication_table_mod import *
try:
    n=input("Enter a number for generate multiplication table:")
    table(n) #function call gives either result,exceptions
except ZeroError:
    print("Dont enter zero as input!")
except NegativeNumError:
    print("Dont Enter negative numbers")
except SpaceError:
    print("Dont leave the input empty!")
except:
    print("Something went wrong!")
    