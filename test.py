from parametric_simulation import run_one_simulation_helper
 
eplus_run_path = '../eplus_test/energyplus9.5/energyplus'
idf_path = '../eplus_test/1ZoneUncontrolled_win1.idf'
parametric_key = ['WindowMaterial:SimpleGlazingSystem','SimpleWindow:DOUBLE PANE WINDOW', 'solar_heat_gain_coefficient']
parametric_val = 0.1
output_dir = './temp_res_1'
run_one_simulation_helper(eplus_run_path, idf_path, output_dir, parametric_key, parametric_val)
