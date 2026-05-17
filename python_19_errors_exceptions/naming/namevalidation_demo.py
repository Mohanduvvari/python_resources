from nameExcept import InvalidNameError,SpaceError,ZeroNameLengthError
from namevalidation import validatename
while(True):
    try:
        name=input("Enter you name:")
        validatename=validatename(name)
    except SpaceError:
        print("Dont Enter space for name")
    except ZeroNameLengthError:
        print("Plase check your name")
    except InvalidNameError:
        print(f"{name} is invalid!")
    except:
        print("OOPS something went wrong")
    else:
        print(f"your name {name} is valid")
        break
