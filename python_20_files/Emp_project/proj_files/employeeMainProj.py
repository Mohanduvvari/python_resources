from empMenu import menu
from empAdd import addemp
from empDel import delemp
from empview import viewemp, viewallemps
from empsearch import searchemp
from empUpdate import updateemp

while True:
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                addemp()
            case 2:
                delemp()
            case 3:
                updateemp()
            case 4:
                viewemp()
            case 5:
                viewallemps()
            case 6:
                searchemp()
            case 7:
                print("\thx for using this project")
                break
            case _:
                print("\tYour selection of operation is invalid - try again")
    except ValueError:
        print("Dont enter alnums,strs,symbols for choice - try again")
            