#Author Liyang Yu
#last edit time 2022/11/22 cw3 has done

import json
import copy
import numpy as np 
from StaticEplusEngine import run_eplus_model, convert_json_idf

def run_one_simulation_helper(eplus_run_path, idf_path, this_output_dir,
	                            parameter_key_1, parameter_val_1,
                                parameter_key_2, parameter_val_2):
    #####step 1 convert idf to json
    convert_json_idf(eplus_run_path,idf_path)
    epjson_path = idf_path.split('.idf')[0] + '.epJSON'
    #####step 2 load josn file into a JSON dict
    with open(epjson_path) as epJSON:
        epjson_dict = json.load(epJSON)
    #####step 3 change the dict json val
    inner_dict = epjson_dict
    for i in range(len(parameter_key_1)):
        if i < len(parameter_key_1) - 1:
            inner_dict = inner_dict[parameter_key_1[i]]
    inner_dict[parameter_key_1[-1]] = parameter_val_1
    inner_dict = epjson_dict
    for j in range(len(parameter_key_2)):
        if j < len(parameter_key_2) - 1:
            inner_dict = inner_dict[parameter_key_2[j]]
    inner_dict[parameter_key_2[-1]] = parameter_val_2
    ######step 4 dump the JSON divt to JSON file
    with open(epjson_path,'w') as epjson:
        json.dump(epjson_dict, epjson)
    ######step 5 convert JSON file to idf 
    convert_json_idf(eplus_run_path, epjson_path)
    ######step 6 
    run_eplus_model(eplus_run_path, idf_path, this_output_dir)
    return this_output_dir



def run_one_parametric_simulation(eplus_run_path, idf_path, output_dir,
	                            parameter_key_1, parameter_vals_1,
                                parameter_key_2, parameter_vals_2):
    print("1")
    the_dict_of_path = {}
    for i in range(len(parameter_vals_1)):
        for j in range(len(parameter_vals_2)):
            this_output_dir = output_dir + '/run_' + str(i+1)
            this_file_path = this_output_dir + '/eplusout.csv'
            the_dict_of_path[str(parameter_vals_1[i]) + str(parameter_vals_2[j])] = this_file_path 
            parameter_val_1 = parameter_vals_1[i]
            parameter_val_2 = parameter_vals_2[j]
            run_one_simulation_helper(eplus_run_path, idf_path, 
                this_output_dir, parameter_key_1, parameter_val_1,
                parameter_key_2, parameter_val_2)
        
    '''
    this is to confirm the dict is correct
    print(the_dict_of_path)
    '''
    return the_dict_of_path
        


