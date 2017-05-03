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
	data = [ ['A', 0, 45], ['.', 46, 255] ]
	print(data)
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
		#print (element[0])
		#for i in range(height*length):
		count = 0
		while (count < (element[2] - element[1])): #and loc < height * length:
			if( (loc-1)%32 == 0 and loc != 0):
				s += "\n"
				#print("newline!")
				nl_count+=1
				print( str(loc - start) ) 
				start = loc
			
			s = s + str(loc)
			s += element[0]
			count  += 1
			loc += 1
			#print(count, loc, nl_count, element[0])
			
			print (element[0])
		print(len(s))
	print(s)

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
	
		
	

