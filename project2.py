from __future__ import print_function
import sys
from Process import *

def initData():
	data = []
	for i in range(8):
		line = []
		for j in range(32):
			line.append('.')
			data.append(line)
	return data

def printData(data):
	print ("="*32)
	for i in range(8):
		for j in range(32):
			print(data[i][j], end ="")
		print("")
	print ("="*32)

''' @param name of input file
	@return a
'''
def parseFile(filename):
	process = []
	num = 0
	for line in open(fileName, "r"):
		temp = (line.strip()).split(" ")
		if(num == 0):
			num  = temp
			continue
		else:
			arrivals = temp[2:]
			# clean input
			for x in range(len(arrivals)):
				arrivals[x] = arrivals[x].split("/")
				arrivals[x][0] = int(arrivals[x][0])
				arrivals[x][1] = int(arrivals[x][1])
			# make object for each time
			
			for x in arrivals:
				new = Process(temp[0], temp[1], x)
				process.append(new)
				print(new)

	return [process, num]
	
	

if __name__ == "__main__":

	#function that starts 256 frames of datat log

	data = initData()
	printData(data)
	fileName = sys.argv[1]
	temp = parseFile(fileName)
	processes = temp[0]
	numProcess = temp[1]
	
		
	

