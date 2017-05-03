from __future__ import print_function
import sys
import Process

def initData():
        data = []
        data.append( ['.', 0, 255] )
        return data

def printData( data ):
        return
        
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
        #printData(data)
        fileName = sys.argv[1]
        temp = parseFile(fileName)
        processes = temp[0]
        numProcess = temp[1]
        print(processes)
        print(numProcess)
        memList = []
        for i in processes:
                for j in i[2]:
                        memList.append(Process(i[0], i[1], j) )
        #for i in processes:
                #print (i)




