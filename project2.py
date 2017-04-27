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
	@return a list of objects type Process
'''

def parseFile(filename):
	process = []
	num = 0
	for line in open(fileName, "r"):
		temp = (line.strip()).split(" ")
		if(num == 0):
			num =temp[0] 	
		else:
			arrivals = temp[2:]
			for x in range(len(arrivals)):
				arrivals[x] = arrivals[x].split("/")
			temp = Process(temp[0], temp[1], arrivals)
			process.append(temp)

	return [process, num]
	
	

if __name__ == "__main__":

	#function that starts 256 frames of data
	data = initData()
	fileName = sys.argv[1]
	temp = parseFile(fileName)
	processes = temp[0]
	numProcess = temp[1]
	
		
	

