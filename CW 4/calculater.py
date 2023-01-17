#### this can work with the typing varible not for GUI  
def read_and_calculate(K_values, ds, n):
         #### need change this is veriable for the GUI how many veriable the user type
    dict_K = {} ####create two dicts for K and d
    dict_d = {}
    i = 0
    x = 0
    while i<n: #### this is for the add the value to the dict
        dict_K[i] = K_values[x]
        dict_d[i] = ds[x]
        i = i + 1
        x = x + 1 
    U_value_2(dict_K, dict_d)
    return U_value_2(dict_K, dict_d)
    
def U_value_2(dict_K, dict_d, n):
    i = 0
    
    R_total = 0
    while i<n:
        R_total += dict_d[i]/dict_K[i] 
        i = i + 1
    U_value_1 = 1/(R_total)
    return U_value_1