from __future__ import print_function
import sys
from Process import *
import sys
sys.argv = "x p2-test-input03.txt".split(" ")
#p2-test-input01.txt
#p2-test-input02.txt
#p2-test-input03.txt



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

def find_dot_loc(data):
	loc = []
	for i in range(len(data)):
		if data[i][0] == ".":
			loc.append(i)
	return loc
def mergeDots(data):
	newData = []
	for i in range(1, len(data)):
		if(data[i-1][0] != "." and data[i][0] != "."):
			newData.append(data[i])
		else:
			newData.append([".", data[i-1][1], data[i][2] ])
			for j in range(i, len(data)):
				newData.append(data[j])
			mergeDots(newData)
	return newData
def nextFitc(data, processes):
	i = 0
	while len(processes) > 0:  #''' and data != all '.'...? '''
		if processes[0].start == i:
			dots = find_dot_loc(data)
		i+=1 
		

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

def contiguous(data, processes):
	nextFitc(data[:], processes[:])
	bestFitc(data[:], processes[:])
	worstFitc(data[:], processes[:])

def nextFitnc():
	pass
def bestFitnc():
	pass
def worstFitnc():
	pass
def non_contiguous():
	pass

def defragmentation(data):
        for element in data:
                if element[0] == '.':
                        data.remove(element)
        lastEnd = 0        
        for element in data:
                len = element[2] - element[1]
                element[1] = lastEnd
                element[2] = element[1] + len
                lastEnd = element[2]
        if ((lastEnd - 256) != 0):
                data.append( [ '.' , lastEnd, 256] )

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

	data = [["A", 0, 45], [".", 45, 256] ]
	printData(data)
	data = mergeDots(data)
	printData(data)
