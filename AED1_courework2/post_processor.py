import pandas as pd 
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def eplus_to_datetime(date_str):
	if date_str[-8:-6] != '24':
		dt_obj = pd.to_datetime(date_str)
	else:
		date_str = date_str[0: -8] + '00' + date_str[-6:]
		dt_obj = pd.to_datetime(date_str) + dt.timedelta(days=1)
	return dt_obj

def plot_1D_results( plot_column_name,
					y_axis_title, plot_title,the_dict_of_path):
	fig, axs = plt.subplots(1, 1, figsize=(20,10))
	fontsize = 20
	for i in the_dict_of_path:  
		this_df = pd.read_csv(the_dict_of_path[i])
		this_df['Date/Time'] = '2002 ' + this_df['Date/Time']
		this_df['Date/Time'] = this_df['Date/Time'].apply(eplus_to_datetime)
		data_st_date = this_df.iloc[0]['Date/Time']
		data_ed_date = this_df.iloc[-1]['Date/Time']
		date_list = this_df['Date/Time']
		this_y = this_df[plot_column_name]
		axs.plot(date_list, this_y,
            	linewidth = 2,
            	label = i)

	datetime_ax_loc = mdates.HourLocator()  
	datetime_ax_fmt = mdates.DateFormatter('%H:%M')
	axs.xaxis.set_major_locator(datetime_ax_loc)
	axs.xaxis.set_major_formatter(datetime_ax_fmt)
	axs.tick_params('x', labelrotation=45)
	axs.set_xlabel('Time (%s to %s)'%(data_st_date, data_ed_date),
				     fontsize = fontsize)
	axs.set_ylabel('Indoor Air Temperature (C)',
              fontsize = fontsize)
	axs.title.set_text(plot_title)
	axs.legend(fontsize = fontsize)
