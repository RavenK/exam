import numpy as np
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
def cal_2nd_col(file):
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
	#return data_list
	
def interval_plot(data):
	list_col_1= []
	for lines in file:
		line = lines.split()
		if len(line) >1:
			col_1 = line[0]
			list_col_1.append(col_1)
	
a = cal_2nd_col(in_file)
print a	

			
		
	
	
	
		
		

		


