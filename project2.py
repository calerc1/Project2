from __future__ import print_function
import sys
from Process import Process


def initData():
    data = []
    data.append(['.', 0, 256])
    return data


def printData(data):
    print ("=" * 32)
    s = ""
    count = 0
    loc = 0
    for element in data:
        count = 0
        while (count < (element[2] - element[1])):
            if((loc) % 32 == 0 and loc != 0):
                s += "\n"
            s += element[0]
            count += 1
            loc += 1
    print(s)
    print ("=" * 32)


def parseFile(filename):
    process = []
    num = 0
    for line in open(fileName, "r"):
        temp = (line.strip()).split(" ")
        if(num == 0):
            num = temp
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


def non_contiguous(data, processes):
    time = 0
    string = 'time '
    string += str(time)
    print('time ' + str(time) + 'ms: Simulator started (Non-contiguous)')
    inMemory = []
    while((len(processes) > 0 or len(inMemory) > 0)):
        # will check for arrivals add them
        # to data and switch from process to inMem
        data = checkDone(data, inMemory, time)
        data = checkReady(processes, data, inMemory, time)
        time += 1
    print('time ' + str(time-1) + 'ms: Simulator ended (Non-contiguous)')


def checkReady(processes, data, inMemory, time):
    i = 0
    end = len(processes)
    while(i < end):
        if(processes[i].start == time):
            print('time ' + str(time) + 'ms: Process ' + processes[i].name
                  + ' arrived (requires ' + str(processes[i].numMem)
                  + ' frames)')
            if(freeSpace(data) >= processes[i].numMem):
                data = nonContiguousAdd(data, processes[i], time)
                inMemory.append(processes[i])
            else:
                print('time ' + str(time) + 'ms: Cannot place process '
                      + processes[i].name + ' -- skipped!')

            printData(data)
            processes.remove(processes[i])
            end -= 1
        else:
            i += 1
    return data


def checkDone(data, inMemory, time):
    i = 0
    end = len(inMemory)
    while(i < end):
        if((inMemory[i].start + inMemory[i].stop) == time):
            print('time ' + str(time) + 'ms: Process '
                  + inMemory[i].name + ' removed:')
            data = deleteProcess(data, inMemory[i].name)
            inMemory.remove(inMemory[i])
            end -= 1
        else:
            i += 1
    return data


def nonContiguousAdd(data, process, time):
    i = 0
    left = process.numMem
    while(left):
        if(data[i][0] == '.'):
            sizeBlock = data[i][2] - data[i][1]
            if(sizeBlock > left):
                data = data[:i] + [[process.name, data[i][1], data[i][1]
                                    + left]] + data[i:]
                data[i+1][1] = data[i][2]
                left = 0
            else:
                data[i][0] = process.name
                left -= sizeBlock
        i += 1
    print('time ' + str(time) + 'ms: Placed process ' + process.name + ':')
    return data


def deleteProcess(data, name):
    i = 0
    end = len(data)
    while(i < end):
        if(data[i][0] == name):
            data[i][0] = '.'
        i += 1
    mergeEverything(data)
    printData(data)
    return data


def defragmentation(data):
    for element in data:
        if element[0] == '.':
            data.remove(element)
    lastEnd = 0
    moved = []
    wait = 0
    for element in data:
        Len = element[2] - element[1]
        if(lastEnd != element[1]):
            moved.append(element[0])
            wait += Len
        element[1] = lastEnd
        element[2] = element[1] + Len
        lastEnd = element[2]
    if ((lastEnd - 256) != 0):
        data.append(['.', lastEnd, 256])
    return [ wait, moved]


def mergeEverything(data):
    i = 0
    end = len(data)
    while((i+1 != end)):
        if(data[i][0] == data[i+1][0]):
            data[i][2] = data[i+1][2]
            data.remove(data[i+1])
            end -= 1
        else:
            i += 1


if __name__ == "__main__":

    data = initData()
    fileName = sys.argv[1]
    temp = parseFile(fileName)
    processes = temp[0]
    numProcess = temp[1]
    processes.sort(key=lambda x: x.start, reverse=False)

   
    non_contiguous(data[:], processes[:])
