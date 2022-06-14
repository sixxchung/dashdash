a_var = range(2)
 
def locals_test():
    b_var = 3
    c_var = "hi"
    d_var = locals()
    print(d_var)
 
locals_test()
 
e_var = globals()
print(e_var)