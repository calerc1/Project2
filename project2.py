from __future__ import print_function
import sys
from Process import *

def initData():
        data = []
        data.append( ['.', 0, 256] )
        return data

       
def printData(data):
	height  = 8
	length = 32
	print ( "=" * 32 )
	s = ""
        count  = 0
	loc = 0
        line = 1
	nl_count = 0
	start = 0
        for element in data:
		count = 0
		while (count < (element[2] - element[1])):
			if( (loc)%32 == 0 and loc != 0):
				s += "\n"
		        s += element[0]
			count  += 1
			loc += 1
			
	print(s)
	print ( "=" * 32 )

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
        return [process, num]

def freeSpace(data):
        space = 0
        for element in data:
                if element[0] == '.':
                        space += (element[2] - element[1])
        return space



def nextFitc():
	pass
def bestFitc():
	pass
def worstFitc():
	pass

def contiguous():
	pass

def nextFitnc():
	pass
def bestFitnc():
	pass
def worstFitnc():
	pass
def non_contiguous():
	pass

def defragmentation(data):
        data = [ ['A', 0, 45], ['.', 45, 64], ['B', 64, 256] ]

        



if __name__ == "__main__":

        print('Init Data')
	data = initData()
        print(freeSpace(data))
	printData(data)
	fileName = sys.argv[1]
	temp = parseFile(fileName)
	processes = temp[0]
	numProcess = temp[1]
        processes.sort(key=lambda x: x.start, reverse=False)
        for i in processes:
                print(i)
	
		
	

