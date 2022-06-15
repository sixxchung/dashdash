# sub/bbb.py
b_var1 = 222

#### for main 
from . import aaa
b_var2 = b_var1 + aaa.a_var


#### for sub-main
# from aaa import a_var
# b_var2 = b_var1 + a_var