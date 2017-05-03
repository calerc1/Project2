from __future__ import print_function
import sys
import Process

def initData():
	data = []
        data.append( ['.', 0, 255] )
	return data

def printData( data ):
        data = [ ['A', 0, 45], ['.', 46, 255] ]
	print ( "=" * 32 )
        current  = 0
        line = 1
        for element in data:
                # final - initial point
                len = element[2] - element[1]
                while (current < element[2]):
                        endLine = line * 32
                        if ( (current + len) >= endLine ):
                                print (element[0] * (endLine - current) ),
                                current = endLine
                                line += 1
                        else:
                                print (element[0] * (len - current) ),
                                current = endLine
                                
                                
	print ("=" * 32)

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
			print(temp)
			

	return [process, num]
	
	

if __name__ == "__main__":

	data = initData()
        print ("Init Memory")
	printData(data)
	fileName = sys.argv[1]
	temp = parseFile(fileName)
	processes = temp[0]
	numProcess = temp[1]
	print(processes)
	print(numProcess)
	
		
	

