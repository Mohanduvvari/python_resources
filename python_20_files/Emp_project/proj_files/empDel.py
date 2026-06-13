import  pickle
def delemp():
    try:
        with open("python_20_files/Emp_project/empfiles/emp.data", "rb") as fp:
            records = []
            while (True):
                try:
                    record = pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
            # display records
            for record in records:
                print(record)
            empno = int(input("Enter Employee Number for Delete the Record:"))
            found = False
            for index in range(len(records)):
                if (records[index][0] == empno):
                    found = True
                    recindex = index
                    break
            if found:
                records.pop(recindex)
                # Place the records from main memory into the file of secondary memory
                with open("D:\\python_resource\\python_resources\\python_20_files\\Emp_project\\empfiles\\emp.data",
                          "wb") as fp:
                    for record in records:
                        pickle.dump(record, fp)
                print("Employee Record deleted--verify")
            else:
                print("Employee Details does not Exist")
    except Exception:
        print("\tFile Not found")
        print("-"*50)