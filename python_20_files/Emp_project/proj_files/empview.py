import pickle
def viewemp():
    try:
        with open("D:\\python_resource\\python_resources\\python_20_files\\Emp_project\\empfiles\\emp.data",
                  "rb") as fp:
            records = []
            while True:
                try:
                    record = pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
            # get emp number form user
            empno = int(input("Enter employee number"))
            found = False
            for record in records:
                if record[0] == empno:
                    recrecord = record
                    found = True
                    break
            print("-" * 50)
            if found:
                print("\tEmployee Number=", recrecord[0])
                print("\tEmployee Name=", recrecord[1])
                print("\tEmployee Salary=", recrecord[2])
                print('\tEmployee Company=', recrecord[3])
            else:
                print(f"\t{empno} Employee not found")
            print("-" * 50)
    except Exception:
        print("\tFile not found")
def viewallemps():
    try:

        with open("D:\\python_resource\\python_resources\\python_20_files\\Emp_project\\empfiles\\emp.data",
                  "rb") as fp:
            print("-" * 50)
            print("\tEmpNo\tName\tSalary\tCompany")
            print("-" * 50)
            while True:
               try:
                   record = pickle.load(fp)
                   for val in record:
                       print(f"\t{val}",end=" ")
                       print()
               except EOFError:
                   print("-" * 50)
                   break
    except Exception:
        print("\tFile not found")

