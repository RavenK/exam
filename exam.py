in_file = open('C:\Users\User\Desktop\hrv\RR.rea')
def find_invalid(in_file):
	count = 0
	for line in in_file:
		count+=1
		for i in line.split():
			if i == "1":
				print count
	return count
file = find_invalid(in_file)
print file