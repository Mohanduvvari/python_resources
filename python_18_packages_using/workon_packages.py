#method-1

# workon_packages.py filename not module we create it for practice on python_18_packages i.e working in some other folder package
# import icici   #this import gives error as this module currently not in this folder

from python_18_packages.Bank_package import icici #import package directly
# from python_18_packages.Bank_package.icici import bname,address,simpint  #this is import function,global vars directly
from python_18_packages.Bank_package import max

print("Your Name: Vamsi")
print("your bank name: ",icici.bname)
print("you bank address: ",icici.address)
icici.simpint()
print("-"*50)
print("finding max values in list")
print("*"*50)
max.findmax()