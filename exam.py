import numpy as np
from matplotlib import pyplot as plt
in_file = open('C:\Users\User\Desktop\hrv\RR.rea')

def find_invalid(file):
	count = -1
	invalid=[]
	for line in file:
		count+=1
		for i in line.split():
			if i == "1":
				invalid.append(count)
	return invalid
def select_column(file,column):
	list_col= []
	for lines in file:
		line = lines.split()
		if len(line) >1:
			col = line[column]
			list_col.append(col)
	list_col[0]=0
	data_list = [float(i) for i in list_col]
	return data_list
def cal_2nd_col():
	in_file.seek(0)
	check = find_invalid(in_file)
	in_file.seek(0)
	data_list = select_column(in_file,1)
	for val in check:
		data_list[val]=0
	max_value = max(data_list)
	min_value = min(data_list)
	average = np.mean(data_list)
	standard_deviation= np.std(data_list)
	print max_value,min_value,average,standard_deviation
	return data_list
	
def interval_plot():
	in_file.seek(0)
	col_1 = select_column(in_file,0)
	in_file.seek(0)
	col_2 = select_column(in_file,1)
	time_1 = 5*60 #5 mins to second
	time_2 = 15*60 #15 mins to second
	for i in col_1:
		print i
			
	time = col_1[0:i]
	plt.plot(time,col_2)
	plt.show()
			
a = interval_plot()
print a	

			
		
	
	
	
		
		

		


