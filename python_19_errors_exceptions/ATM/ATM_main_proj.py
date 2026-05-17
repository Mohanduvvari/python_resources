from ATMExceptions import DepositError,WithdrawError,InsuffFundError
from ATM_Menu import menu
from ATM_Operations import deposit,withdraw,balenq

while True:
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                try: 
                    deposit()
                except DepositError:
                    print("Dont Enter zero or -ve values for deposit")
                except ValueError:
                    print("Dont Enter Alnums,str and symbols for deposit")              
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("Dont Enter zero or -ve")
                except ValueError:
                    print("Dont Enter Alnums,str,symbols")
                except InsuffFundError:
                    print("Your Account should not have insufficent amount, min amount is 500")
            case 3:
                balenq()
            case 4:
                print("Thank you for using my Operations")
                break
            case _:
                print("You choose wrong operation, Try Again")
    except ValueError:
        print("Dont Enter alnums, strs, symbols for choice - Try again")