# ATM_Operations           ---- module
from ATMExceptions import DepositError,WithdrawError,InsuffFundError

bal=500.00  #initial balance, min amount in the account 
def deposit():
    Damnt=float(input("Enter Your Amount")) #possible of valueerror
    if Damnt<=0:
        raise DepositError
    else:
        global bal
        bal=bal+Damnt
        print(f"Your account XXXXXXX credited with {Damnt}")
        print(f"Now your balance is {bal}")
def withdraw():
    global bal
    Wamnt=float(input("Enter your withdraw amount:")) #possible value error
    if Wamnt<=0:
        raise WithdrawError
    else:
        if (Wamnt+500)>bal:
            raise InsuffFundError
        else:
            bal=bal-Wamnt
            print(f"Your account debited with {Wamnt}")
            print(f"Now your account balance is {bal}")
def balenq():
    print("Your account balance:{}".format(bal))
