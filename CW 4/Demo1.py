#### author：Liyang 
#### date: 2022/12/23
####this is the packedge for the chart of material 
class Material():
    def __init__(self, K_value, d):
        self.K_value = K_value
        self.d = d

material1 = Material(K_value = '0.12' , d = '0.01')
material2 = Material(K_value = '0.24' , d = '0.01')
material3 = Material(K_value = '0.36' , d = '0.01')
#######


#####this for the def a function to calculate the U_value
####n = "the_number_of_input"
k=0
d=0
def U_value(k,d,x):
    i=1
    while i < 3:
        print(i)
        x = 'material' + str(i)
        print(x)
        k = x.K_value
        d = x.d
        print(k)
        print(d)
        i = i + 1
####another way to solve the stordege of K,d
#### this can work with the typing varible not for GUI  
def read_and_calculate(K_values, ds):
    n = 3       #### need change this is veriable for the GUI how many veriable the user type
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
    
def U_value_2(dict_K, dict_d):
    i = 0
    n = 3
    R_total = 0
    while i<n:
        R_total += dict_d[i]/dict_K[i] 
        i = i + 1
    U_value_1 = 1/(R_total)
    return U_value_1



