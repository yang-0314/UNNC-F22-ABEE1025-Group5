#### Author: Liyang YU & Zesheng YANG
#### Last modified: 2023-01-27
#### The following programdemostrate how to read and calculate 
#### the U-value of building elements
#### this can work with the typing varible not for GUI  

def read_and_calculate(K_values, ds, n):
    #### This is veriable for the GUI how many veriable the user type
    #### create two dicts for K and d    
    dict_K = {}   #### the dict for K-value
    dict_d = {}   #### the dict for Material Thickness
    i = 0     #### i the number in dic_K and dic_d
    x = 0     #### x the number in K_values and ds
    while i < n:    #### This loop is to add the data to the dictionary
        dict_K[i] = K_values[x]
        dict_d[i] = ds[x]
        i = i + 1
        x = x + 1 
    U_value_2(dict_K, dict_d)
    return U_value_2(dict_K, dict_d)
    
def U_value_2(dict_K, dict_d, n):
    i = 0
    R_total = 0   #### the original R-value is 0
    while i < n:
        R_total += dict_d[i]/dict_K[i] 
        #### Thermal Resistance = 
        #### Material Thickness / Thermal Conductivity
        #### to add each layers up 
        #### is the total thermal resistances
        i = i + 1
    U_value_1 = 1/(R_total)
    #### The U-value of a building element 
    #### is the inverse of the total thermal resistances 
    #### of the different layers making up the building element.
    return U_value_1
