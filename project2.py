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



def freeSpace(data):
        space = 0
        for element in data:
                if element[0] == '.':
                        space += (element[2] - element[1])
        return space



def nextFitc(data, processes):
	print("Start nextfit")
	printData(data)
	for el in processes:
		print(el)
	i = 0
	isempty = True
	while len(processes) > 0  and i <= 100:
		#printData(data)
		#if Process leaves at time i
		
		#if Process arrives at time i
		if(processes[0].start == i):
			print("TRIGGERED", i, processes[0].numMem)
			length = processes[0].numMem
			dots = find_dot_loc(data)
			print(dots)
			if(len(dots) > 0):
				for x in dots:
					dstart = data[x][1]
					dend = data[x][2]
					dlength = data[x][2] - data[x][1]
					print(dlength, length)
					print (dlength > length)
					if dlength >= length:
						print("here")
						data.insert(x, [processes[0].name, dstart, dstart + length] )
						data.pop(x+1)
						printData(data)
						if length < dlength:
							data.insert(x+1, [".", dstart + length, dend ])
						printData(data)
			else:
				pass #unable to place process
		i+=1
	

def bestFitc(data, processes):
	pass
def worstFitc(data, processes):
	pass

def contiguous(data, processes):
	nextFitc(data[:], processes[:])
	bestFitc(data[:], processes[:])
	worstFitc(data[:], processes[:])




def nextFitnc(data, processes):
        time = 0 
        inMemory = []
        
        while(processes > 0 and inMemory > 0):
              #will check for arrivals add them to data and switch from process to inMem
              checkReady(processes, data, inMemory)

              checkDone(data, inMemory)

              time +=1
                
                
def checkReady(processes, data, inMemory):
        #
        i = 0
        end = 0 
        while( i+1 != end):
   			if( processes[i].start == time):
   				inMemory.append(processes[i])
   				processes.remove(i)
   				end -= 1
   			else:
   				i += 1



def bestFitnc():
	pass
def worstFitnc():
	pass
def non_contiguous(data, processes):
	nextFitnc(data[:], processes[:])

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
                data.append(['.', lastEnd, 256])
                

def mergeEverything(data):
        i=0
        end  = len(data)
        while( (i+1 != end)  ):
                if( data[i][0] == data[i+1][0]):
                        data[i][2] = data[i+1][2]
                        data.remove(data[i+1])
                        end -= 1
                else:
                        i += 1



if __name__ == "__main__":
	print('Init Data')
	data = initData()
	printData(data)
	fileName = sys.argv[1]
	temp = parseFile(fileName)
	processes = temp[0]
	numProcess = temp[1]
	processes.sort(key=lambda x: x.start, reverse=False)

    for i in processes:
        print (i)
        '''
	contiguous(data, processes)
	'''
    for i in processes:
        print(i)
	'''
		
	data = [["A", 2, 45], [".", 45, 75], ["B", 75, 100], [".", 100, 256] ]
        '''


    non_contiguous(data, processes)
	'''data = [["A", 0, 45], [".", 45, 256] ]

	printData(data)
	print( "Go\n", mergeDots(data) )
	printData(data)
      '''

        #mergeeverything test
        '''
        data = [ ['A', 0, 20], ['.',20,40], ['.',40,60], ['B',60,80], ['B',80, 256] ]
        printData(data)
        print (data)
        mergeEverything(data)
        printData(data)
        '''
        # freeSpace test
        '''
        print(freeSpace(data))
        data = [ ['A', 0, 20], ['.',20,40], ['.',40,60], ['B',60,80], ['B',80, 256] ]
        mergeEverything(data)
        print(freeSpace(data))
        '''

        #defragmentation test
        '''
        data = [ ['A', 0, 20], ['.',20,40], ['.',40,60], ['B',60,80], ['B',80, 256] ]
        mergeEverything(data)

        printData(data)
        defragmentation(data)
        printData(data)
        '''

S