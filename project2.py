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
        for element in data:
		count = 0
		while (count < (element[2] - element[1])) and loc < height * length:
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


if __name__ == "__main__":

        print('Init Data')
	data = initData()
	printData(data)
	fileName = sys.argv[1]
	temp = parseFile(fileName)
	processes = temp[0]
	numProcess = temp[1]
	
		
	

