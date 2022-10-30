######last edit in 2022/10/30
from matplotlib import pyplot as plt 
from parametric_simulation import run_one_parametric_simulation
from post_processor import plot_1D_results
##########This step is for confirm the range of parameter_vals
test_range = list(range(25,75,2))
for item in range(25):
    test_range[item] = test_range[item]/100

##########Tell the varible of run_one_parametric_simulation
eplus_run_path = '../eplus_test/energyplus9.5/energyplus'
idf_path = '../eplus_test/1ZoneUncontrolled_win_1.idf'
parameter_key = ['WindowMaterial:SimpleGlazingSystem', 
                'SimpleWindow:DOUBLE PANE WINDOW',
                'solar_heat_gain_coefficient']
output_dir = '../eplus_test/param_exp_1'
parameter_vals = test_range

##########tell the varible of plot_cloumn_name
the_dict_of_path = run_one_parametric_simulation(eplus_run_path, idf_path, 
                    output_dir, 
                    parameter_key, parameter_vals)
plot_cloumn_name = 'ZONE ONE:Zone Mean Air Temperature [C](TimeStep) '
y_axis_title = 'Indoor Air Temperature [C](TimeStep)'
plot_title = 'Simulation of Indoor Air Temperature vs. SHCG'
plot_1D_results( plot_cloumn_name, y_axis_title, 
                plot_title, the_dict_of_path)
##########save the figure
plt.savefig('plot_1D_results')

