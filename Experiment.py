import sys

def largest(inlist):
	if len(inlist) == 0:
		raise ValueError("Cannot call largest on empty list")
	max = -sys.maxint # "smallest" possible int
	# max = 0
	for index in range(len(inlist)):
		if (inlist[index] > max):
			max = inlist[index]
			return max

def average(inlist):
	if len(inlist) == 0:
		raise ValueError("Cannot call average on empty list")

	sum = 0
	for num in inlist:
		try:
			f_num = float(num)
		except ValueError:
			raise ValueError("Non-number element in list")
		else:
			sum += f_num
	return sum/len(inlist)