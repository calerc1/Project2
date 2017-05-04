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
	tempData = []
	newData = []
	for i in data:
		if i[0] != ".":
			tempData.append(i)
	print(tempData)
	if(len(tempData) == 0 ):
		return initData()
	
	print(tempData)	
	i = 0
	end = len(data)
	while i < len(tempData):
		if(len(tempData) == 1 ):
			if(tempData[0][1] != 0):
				tempData.insert(0, [".", 0, tempData[0][1]])
			if(tempData[0][2] != 256):
				tempData.append([".", tempData[0][2], 256 ])		
		if(tempData[i - 1][2] != tempData[i][1]):
			newData.append([ ".", tempData[i - 1][2], tempData[i][2] ] )
		else:
			newData.append(tempData[i-1])
	i+=1
	
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



def nextFitc(data, processes):
	i = 0
	isempty = True
	while len(processes > 0):
		if(processes[0].start == i):
			length = processes[0].numMem
			dots = find_dot_loc(data)
			if(len(dots) > 0):
				for x in dots:
					dstart = data[x][1]
					dend = data[x][2]
					dlength = data[x][2] - data[x][1]
					if dlength >= length:
						data.insert(x, [processes[0].name, dstart, dstart + length] )
						if length < dlength:
							data.insert(x+1, [".", dstart + length, dend ])
			else:
				pass #unable to place process
		i+=1

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
        data = [ ['A', 0, 45], ['.', 45, 64], ['B', 64, 256] ]

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

        for i in processes:
                print(i)
	
		
	data = [["A", 2, 45], [".", 45, 75], ["B", 75, 100], [".", 100, 256] ]

	printData(data)
	print( "Go\n", mergeDots(data) )
	printData(data)


        
