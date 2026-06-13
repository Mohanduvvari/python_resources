import pickle
def searchemp():
  try:
    with open("D:\\python_resource\\python_resources\\python_20_files\\Emp_project\\empfiles\\emp.data","rb") as fp:
        records=[]
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
        #get emp number form user
        empno=int(input("Enter Emp Number to search:"))
        found=0
        for record in records:
            if record[0]==empno:
                found=1
                break
        print("-"*50)
        if found:
            print('\tEmployee Found and valid')
            print("\tEmpno\tName\tSalary\tCompany")
            print(f"\t{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")
        else:
            print("\tEmployee not found and in-valid")
        print('-'*50)
  except Exception:
      print("\tFile not found")
      print("-"*50)