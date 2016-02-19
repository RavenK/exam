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
	
	check = find_invalid(in_file)
	in_file.seek(0)
	data_list = select_column(in_file,1)
	for val in check:
		data_list[val]=0
	max_value = max(data_list)
	min_value = min(data_list)
	average = np.average(data_list)
	standard_deviation= np.std(data_list)
	return max_value,min_value,average,standard_deviation
def five_min_plot():
	
	col_1 = select_column(in_file,0)
	in_file.seek(0)
	col_2 = select_column(in_file,1)
	time = 5
	
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
	
	col_1 = select_column(in_file,0)
	in_file.seek(0)
	col_2 = select_column(in_file,1)
	time = 15
	
	stop=0
	for i in range(len(col_1)):
		if col_1[i] < time:
			stop=i	
	time = col_1[0:stop]
	new_col_2 = col_2[0:stop]
	#plt.plot(time,new_col_2)
	#plt.xlabel('time (s)')
	#plt.ylabel('values')
	#plt.title ('15 minutes datas')
	#plt.show()
	#This function will be recall in segment_plot function
	#so I hide the plot of it. If not, the segment_plot will plot
	#2 plots of fifteen_min_plot and segment_plot.
	return stop	
def whole_values_plot():

	
	col_2 = select_column(in_file,1)
	plt.hist([col_2], bins = 100)
	plt.title("Histogram of RR time series")
	plt.xlabel("Values")
	plt.ylabel("Frequency")
	plt.annotate("maximum",xy = (661.55,7483.15),xytext = (741.144,7780.49), arrowprops=dict(facecolor='black', shrink=0.05))
	plt.annotate("minimum",xy = (214.724,16.2602),xytext = (314.467,402.439), arrowprops=dict(facecolor='black', shrink=0.05))
	plt.annotate("average",xy = (728.994,3325.84),xytext = (957.776,3845.51), arrowprops=dict(facecolor='black', shrink=0.05))
	plt.show()
def segment_plot():	
	
	col_2 = select_column(in_file,1)
	in_file.seek(0)
	step=fifteen_min_plot()
	lists = [col_2[i:i+step] for i in range(0,len(col_2),step)]
	average=[]
	time=[]
	for i in range(len(lists)):
		mean = np.average(lists[i])
		time.append(i)
		average.append(mean)
	plt.xlabel("Time (min)")	
	plt.ylabel("Average")
	plt.title("Segments of Electrical Heart Datas in every 15 mins")
	plt.plot(time,average)
	plt.show()

	
			
#a = find_invalid(in_file)
#print a
#b= cal_2nd_col()
#print b
#c=five_min_plot()
#print c
#d = fifteen_min_plot()
#print d
#e= whole_values_plot()
#print e
#f= segment_plot()
#print f
		
	
	
	
		
		

		


