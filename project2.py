from __future__ import print_function
import sys
from Process import *

def initData():
        data = []
        data.append( ['.', 0, 255] )
        return data

       
''' @param name of input file
@return a list of objects type Process
'''
def printData(data):
        return

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


	data = initData()
	printData(data)
	fileName = sys.argv[1]
	temp = parseFile(fileName)
	processes = temp[0]
	numProcess = temp[1]
	
		
	

