#Author Liyang Yu
#time 2022/10/22

import json
import copy
import numpy as np 
from StaticEplusEngine import run_eplus_model, convert_json_idf

def run_one_simulation_helper(eplus_run_path, idf_path, this_output_dir,
	                            parameter_key, parameter_val):
    #####step 1 convert idf to josn
    convert_json_idf(eplus_run_path,idf_path)
    epjson_path = idf_path.split('.idf')[0] + '.epJSON'
    #####step 2 load josn file into a JSON dict
    with open(epjson_path) as epJSON:
        epjson_dict = json.load(epJSON)
    #####step 3 change the dict json val
    inner_dict = epjson_dict
    for i in range(len(parameter_key)):
        if i < len(parameter_key) - 1:
            inner_dict = inner_dict[parameter_key[i]]
    inner_dict[parameter_key[-1]] = parameter_val
    ######step 4 dump the JSON divt to JSON file
    with open(epjson_path,'w') as epjson:
        json.dump(epjson_dict, epjson)
    ######step 5 convert JSON file to idf 
    convert_json_idf(eplus_run_path, epjson_path)
    ######step 6 
    run_eplus_model(eplus_run_path, idf_path, this_output_dir)
    return this_output_dir


'''
parameter_vals = np.arange(0.25, 0.75, 0.02)
'''
def run_one_parametric_simulation(eplus_run_path, idf_path, output_dir,
	                            parameter_key, parameter_vals):
    
    the_dict_of_path = {}
    for i in range(len(parameter_vals)):
        this_output_dir = output_dir + '/run_' + str(i+1)
        this_file_path = this_output_dir + '/eplusout.scv'
        parameter_val = parameter_vals[i]
        run_one_simulation_helper(eplus_run_path, idf_path, 
                this_output_dir, parameter_key, parameter_val)
        the_dict_of_path[str(parameter_vals[i])] = this_file_path 
    print(the_dict_of_path)
        


   