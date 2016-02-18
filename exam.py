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
	
def cal_2nd_col(file):
	list_col_2= []
	for lines in file:
		line = lines.split()
		if len(line) >1:
			col_2 = line[1]
			list_col_2.append(col_2)
	
	in_file.seek(0)
	check = find_invalid(in_file)
	list_col_2[0]=0
	data_list = [float(i) for i in list_col_2]
	for val in check:
		data_list[val]=0
		
	max_value = max(data_list)
	min_value = min(data_list)
	average = np.mean(data_list)
	standard_deviation= np.std(data_list)
	print max_value,min_value,average,standard_deviation
	return data_list
	
def plot
	

			
		
	
	
	
		
		

		



a= cal_2nd_col(in_file)
print a
