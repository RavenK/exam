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
	return max_value,min_value,average,standard_deviation
def five_min_plot():
	in_file.seek(0)
	col_1 = select_column(in_file,0)
	in_file.seek(0)
	col_2 = select_column(in_file,1)
	time = 5*60 #5 mins to second
	
	stop=0
	for i in range(len(col_1)):
		if col_1[i] < time:
			stop=i	
	time = col_1[0:stop]
	new_col_2 = col_2[0:stop]
	plt.plot(time,new_col_2)
	plt.xlabel('time (s)')
	plt.ylabel('values')
	plt.title('5 minutes datas')
	plt.show()
def fifteen_min_plot():
	in_file.seek(0)
	col_1 = select_column(in_file,0)
	in_file.seek(0)
	col_2 = select_column(in_file,1)
	time = 15*60 #5 mins to second
	
	stop=0
	for i in range(len(col_1)):
		if col_1[i] < time:
			stop=i	
	time = col_1[0:stop]
	new_col_2 = col_2[0:stop]
	plt.plot(time,new_col_2)
	plt.xlabel('time (s)')
	plt.ylabel('values')
	plt.title ('15 minutes datas')
	plt.show()
def whole_values_plot():

	in_file.seek(0)
	col_2 = select_column(in_file,1)
	plt.hist([col_2], bins = 100)
	plt.title("Histogram of RR time series")
	plt.xlabel("Values")
	plt.ylabel("Frequency")
	plt.annotate("maximum",xy = (661.55,7483.15),xytext = (741.144,7780.49), arrowprops=dict(facecolor='black', shrink=0.05))
	plt.annotate("minimum",xy = (214.724,16.2602),xytext = (314.467,402.439), arrowprops=dict(facecolor='black', shrink=0.05))
	plt.annotate("average",xy = (728.994,3325.84),xytext = (957.776,3845.51), arrowprops=dict(facecolor='black', shrink=0.05))
	plt.show()
	
	
			
#a = five_min_plot()
#print a
#b = fifteen_min_plot()
#print b
c= whole_values_plot()
print c
d= cal_2nd_col()
print d			
		
	
	
	
		
		

		


