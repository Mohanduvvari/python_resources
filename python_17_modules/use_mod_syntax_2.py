# here we import all created modules and use them.

# import mod_icici,mod_aop,mod_mathsinfo 
#--------------------------------------------------------
# import mod_aop as ap
# import mod_icici as ic
# import mod_mathsinfo as mi
# -------------------------------------------------------------
import mod_aop as ap, mod_icici as ic, mod_mathsinfo as mi
print("val of PI=",mi.pi)
print("val of E=",mi.e)
print("-"*50)
ap.sumop(100,5)
ap.mulop(25,5)
print("-"*50)
print("Branch of my bank is=",ic.bname)
ic.simpint()