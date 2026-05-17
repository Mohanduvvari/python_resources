#method-2
#this method is access packages using sys.path.append from another folder,drive
import  sys
sys.path.append("D:\\python_resource\\python_resources\\python_18_packages\\Bank_package")
import icici  #here even the importing looks like error but is correct
print(icici.bname)
print(icici.address)
icici.simpint()
