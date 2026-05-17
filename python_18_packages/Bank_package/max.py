# max.py filename/modulename in package Bank_package

def findmax():
    n=int(input("Enter how many numbers you have: "))
    if n<=0:
        print(f"{n} is invalid")
    else:
        lst=[]
        for i in range(n):
            val=float(input(f"Enter {i} value: "))
            lst.append(val)
        print(lst)
        max=lst[0]
        for val in lst:
            if val>max:
                max=val
        else:
            print(f"max of{lst} ={max}")
