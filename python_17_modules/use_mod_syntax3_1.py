#here we using form modulename import var,func,class 

from mod_mathsinfo import pi,e
from mod_aop import sumop,subop,divop #............
from mod_icici import bname,address,simpint
# ----------------------------------------------------
# from mod_aop import sumop as sum,subop as sub, mulop as prod
# from mod_icici import bname as bank,address as adr,simpint as intrest
# from mod_mathsinfo import pi as pi, e as e
#----------------------------------------------------------------
print("Pi value=",pi)
print("E value = ",e)
print('-'*50)
sumop(100,16)
subop(100,16)
divop(100,16)
print("-"*50)
print("Bank name:",bname)
print("Address:",address)
simpint()
