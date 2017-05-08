''' Group Members: Austin Egri, Sumit Munshi And Carlos Calero '''

from __future__ import print_function
import sys
from Process import Process


def initData():
    data = []
    data.append(['.', 0, 256])
    return data


def printData(data):
    print("=" * 32)
    s = ""
    count = 0
    loc = 0
    for element in data:
        count = 0
        while (count < (element[2] - element[1])):
            if ((loc) % 32 == 0 and loc != 0):
                s += "\n"
            s += element[0]
            count += 1
            loc += 1
    print(s)
    print("=" * 32)


def parseFile(filename):
    process = []
    num = 0
    for line in open(fileName, "r"):
        temp = (line.strip()).split(" ")
        if (num == 0):
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


'''
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
'''


def find_dot_loc(data):
    loc = []
    for i in range(len(data)):
        if data[i][0] == ".":
            loc.append(i)
    return loc


'''
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
'''


def freeSpace(data):

    space = 0
    for element in data:
        if element[0] == '.':
            space += (element[2] - element[1])
    return space


def arrival_endReady(processes, i, data):
    arrival = []
    end = []
    for j in range(len(processes)):
        if (processes[j].start == i):
            arrival.append(j)
        if (processes[j].stop == i):
            # print(processes[j].name)
            for k in range(len(data)):
                if (data[k][0] == processes[j].name):
                    # print(k, data[k][0])
                    end.append([j, k])
    return (arrival, end)


def setLoc(endLoc, data, size):
    # print("Finding EndLoc:", endLoc)
    dots = find_dot_loc(data)
    if (len(dots) == 0 or size > freeSpace(data)):
        # print("Same EndLoc: h0", endLoc)
        return endLoc
    if (len(dots) == 1):
        # ("New EndLoc: h0", data[dots[0]][1])
        return data[dots[0]][1]
    i = 0
    while i < len(dots):
        if endLoc in range(data[dots[i]][1], data[dots[i]][2]):
            if (data[dots[i]][2] - endLoc >= size):
                # print("New EndLoc: h1", endLoc)
                return endLoc
            '''
            else:
                endLoc = data[dots[i]][2]
                print("New EndLoc: h2", endLoc)
            '''
        i += 1

    i = 1
    endLoc %= 255
    # print("New EndLoc: ", endLoc)
    while i < len(dots):
        # print("i:", i)
        if (endLoc >= data[dots[i - 1]][1] and endLoc < data[dots[i - 1]][2]):
            if (data[dots[i - 1]][2] - endLoc >= size):
                # print("New EndLoc: h1", endLoc)
                return endLoc
            else:
                endLoc = data[dots[i]][1]
                # print("New EndLoc: h2", endLoc)
        if endLoc >= data[dots[i - 1]][2] and endLoc < data[dots[i]][1]:
            if (data[dots[i]][2] - endLoc >= size):
                # print("New EndLoc: h3", data[dots[i]][1])
                return data[dots[i]][1]
            else:
                endLoc = data[dots[i]][2]
                # print("New EndLoc: h4", endLoc)
        i += 1

    # print("New EndLoc: h5", data[dots[0]][1])
    return data[dots[0]][1]


def nextFitc(data, processes):
    print("time 0ms: Simulator started (Contiguous -- Next-Fit)")
    # printData(data)
    '''
    for el in processes:
            print(el)
    '''
    endLoc = 0
    i = 0
    hasArrivals = False
    hasExits = False
    while len(processes) > 0:
        endLoc = endLoc % (32 * 8)
        # s = ""
        # for x in processes:
        # s = s + " " + str(x)
        # print("i:", str(i), s)
        arrivals, exits = arrival_endReady(processes, i, data)
        if len(arrivals) > 0:
            hasArrivals = True
        if len(exits) > 0:
            hasExits = True
        # print("i:", i, arrivals, exits)
        # if Process leaves at time i
        if (hasExits):
            for j in exits:
                s = "time " + str(
                    i) + "ms: Process " + data[j[1]][0] + " removed:"
                print(s)
                '''
                print("i:", i, "Exit:",processes[j].name, processes[j].numMem)
                '''
                dstart = data[j[1]][1]
                dend = data[j[1]][2]
                data.pop(j[1])
                data.insert(j[1], [".", dstart, dend])
                # printData(data)
                mergeEverything(data)
                printData(data)
            hasExits = False

        # if Process arrives at time i
        if (hasArrivals):

            for j in arrivals:
                isPlaced = False
                s = "time " + str(i) + "ms: Process " + processes[j].name + " arrived (requires " + str(processes[j].numMem) + " frames)"
                print(s)
                '''
                print("i:", i, "Enter:",
                processes[j].name, processes[j].numMem)
                '''
                length = processes[j].numMem
                # print(dots)
                dots = find_dot_loc(data)
                if (len(dots) > 0):
                    endLoc = setLoc(endLoc, data, length)
                    for x in dots:
                        if (endLoc in range(data[x][1], data[x][2])):
                            # print(processes[j].name)
                            dstart = data[x][1]
                            dend = data[x][2]
                            dlength = data[x][2] - data[x][1]
                            # print(dlength, length)
                            # print (dlength > length)
                            if dlength >= length:
                                isPlaced = True
                                # print("here")
                                # print(data)
                                data.insert(x, [
                                    processes[j].name, endLoc, endLoc + length
                                ])
                                data.pop(x + 1)
                                # printData(data)
                                if length < dlength:
                                    data.insert(x + 1,
                                                [".", endLoc + length, dend])
                                if (endLoc != dstart):
                                    data.insert(x, [".", dstart, endLoc])
                                # check left
                                endLoc += length
                                # print(endLoc)
                                s1 = "time " + str(i) + "ms: Placed process " + processes[j].name + ":"
                                print(s1)
                                printData(data)
                            break

                # unable to place process
                if(isPlaced is False):
                    if (length <= freeSpace(data)):
                        # enterDefragmentation
                        temp = defragmentation(data)
                        data = temp[0]
                        defragValue = temp[1]
                        pList = temp[2]
                        # # DEFRAG CODE HERE ##
                        s1 = "time " + str(i) + "ms: Cannot place process " + processes[j].name + " -- starting defragmentation"
                        print(s1)
                        # defragValue = 210
                        i += defragValue
                        string = ''
                        l = 0
                        while (l < len(pList) - 1):
                            string += pList[l]
                            string += ', '
                            l += 1
                        string += pList[len(pList) - 1]
                        s1 = "time " + str(
                            i) + "ms: Defragmentation complete (moved " + str(
                                defragValue) + " frames: " + string + ')'
                        print(s1)
                        printData(data)
                        dots = find_dot_loc(data)
                        endLoc = setLoc(endLoc, data, length)
                        for x in dots:
                            # print(data[x][1])
                            # print( data[x][2])
                            if (endLoc in range(data[x][1], data[x][2])):
                                # print(processes[j].name)
                                dstart = data[x][1]
                                dend = data[x][2]
                                dlength = data[x][2] - data[x][1]
                                # print(dlength, length)
                                # print (dlength > length)
                                if dlength >= length:
                                    isPlaced = True
                                    # print("here")
                                    # print(data)
                                    data.insert(x, [
                                        processes[j].name, endLoc,
                                        endLoc + length
                                    ])
                                    data.pop(x + 1)
                                    # printData(data)
                                    if length < dlength:
                                        data.insert(x + 1, [
                                            ".", endLoc + length, dend
                                        ])
                                    if (endLoc != dstart):
                                        data.insert(x, [".", dstart, endLoc])
                                    # check left
                                    endLoc += length
                                    # print(endLoc)
                                    k = 0
                                    while k < len(processes):
                                        processes[k].start += defragValue
                                        processes[k].stop += defragValue
                                        k += 1
                                    s1 = "time " + str(i) + "ms: Placed process " + processes[j].name + ":"
                                    print(s1)
                                    printData(data)
                                break

                    else:
                        s1 = "time " + str(i) + "ms: Cannot place process " + processes[j].name + " -- skipped!"
                        print(s1)
                        exits.append([j, -1])
                        # printData(data)
            hasArrivals = False
        newProcesses = []
        j = 0
        add = True
        while j < len(processes):
            add = True
            # if(len(exits) > 0):

            # print()
            # for x in processes:
            # print(x)

            for exit in exits:
                if exit[0] == j:
                    add = False
                # print("Removing loc", j, "in processes", processes[j])
            if (add):
                newProcesses.append(processes[j])
            j += 1
        # print("len newProcesses:", len(newProcesses))
        processes = createTemp(newProcesses)
        if (len(processes) == 0):
            break
        i += 1
    s = "time " + str(i) + "ms: Simulator ended (Contiguous -- Next-Fit)"
    print(s)


def bestFitc(data, processes):
    print("time 0ms: Simulator started (Contiguous -- Best-Fit)")
    i = 0
    hasArrivals = False
    hasExits = False
    while len(processes) > 0:
        # s = ""
        # for x in processes:
        # s = s + " " + str(x)
        # print("i:", str(i), s)
        arrivals, exits = arrival_endReady(processes, i, data)
        if len(arrivals) > 0:
            hasArrivals = True
        if len(exits) > 0:
            hasExits = True
        # print("i:", i, arrivals, exits)
        # if Process leaves at time i
        if (hasExits):
            for j in exits:
                s = "time " + str(
                    i) + "ms: Process " + data[j[1]][0] + " removed:"
                print(s)
                # print("i:", i, "Exit:", processes[j].name, processes[j].numMem)
                dstart = data[j[1]][1]
                dend = data[j[1]][2]
                data.pop(j[1])
                data.insert(j[1], [".", dstart, dend])
                # printData(data)
                mergeEverything(data)
                printData(data)
            hasExits = False

        # if Process arrives at time i
        if (hasArrivals):
            for j in arrivals:
                isPlaced = False
                s = "time " + str(
                    i
                ) + "ms: Process " + processes[j].name + " arrived (requires " + str(
                    processes[j].numMem) + " frames)"
                print(s)
                length = processes[j].numMem
                # print(dots)
                dots = find_dot_loc(data)
                loc = bestLoc(dots, data, length)
                if loc >= 0:
                    isPlaced = True
                    dstart = data[loc][1]
                    dend = data[loc][2]
                    dlength = data[loc][2] - data[loc][1]
                    # print("here")
                    # print(data)
                    data.insert(loc,
                                [processes[j].name, dstart, dstart + length])
                    data.pop(loc + 1)
                    # printData(data)
                    if length < dlength:
                        data.insert(loc + 1, [".", dstart + length, dend])
                    if (data[loc][1] != dstart):  # THIS SHOULD BE UNNECESSARY
                        data.insert(loc, [".", dstart])
                    s1 = "time " + str(
                        i) + "ms: Placed process " + processes[j].name + ":"
                    print(s1)
                    printData(data)
                # unable to place process
                if (isPlaced is False):
                    if (length <= freeSpace(data)):
                        # enterDefragmentation
                        temp = defragmentation(data)
                        data = temp[0]
                        defragValue = temp[1]
                        pList = temp[2]
                        s1 = "time " + str(
                            i
                        ) + "ms: Cannot place process " + processes[j].name + " -- starting defragmentation"
                        print(s1)
                        # # DEFRAG CODE HERE ##
                        defragValue = 210
                        i += defragValue
                        string = ''
                        l = 0
                        while (l < len(pList) - 1):
                            string += pList[l]
                            string += ', '
                            l += 1
                        string += pList[len(pList) - 1]
                        s1 = "time " + str(
                            i) + "ms: Defragmentation complete (moved " + str(
                                defragValue) + " frames: " + string + ")"
                        print(s1)
                        printData(data)
                        dots = find_dot_loc(data)
                        loc = bestLoc(dots, data, length)
                        if loc >= 0:
                            isPlaced = True
                            dstart = data[loc][1]
                            dend = data[loc][2]
                            dlength = data[loc][2] - data[loc][1]
                            # print("here")
                            # print(data)
                            data.insert(loc, [
                                processes[j].name, dstart, dstart + length
                            ])
                            data.pop(loc + 1)
                            # printData(data)
                            if length < dlength:
                                data.insert(loc + 1,
                                            [".", dstart + length, dend])
                            if (data[loc][1] !=
                                    dstart):  # THIS SHOULD BE UNNECESSARY
                                data.insert(loc, [".", dstart])
                            k = 0
                            while k < len(processes):
                                processes[k].start += defragValue
                                processes[k].stop += defragValue
                                k += 1
                            s1 = "time " + str(
                                i
                            ) + "ms: Placed process " + processes[j].name + ":"
                            print(s1)
                            printData(data)

                        # exits.append([j, -1])
                    else:
                        s1 = "time " + str(
                            i
                        ) + "ms: Cannot place process " + processes[j].name + " -- skipped!"
                        print(s1)
                        exits.append([j, -1])
                        # printData(data)
            hasArrivals = False
        newProcesses = []
        j = 0
        add = True
        while j < len(processes):
            add = True
            # print("time " + str(i) + "ms: Eliminating processes")
            '''
            print()
            s1 = ""
            for x in processes:
                    s1 += str(x) + "\n"
            print (s1)
            '''
            for exit in exits:
                if exit[0] == j:
                    add = False
                    # print("Removing loc", j, "in processes", processes[j])
            if (add):
                newProcesses.append(processes[j])
            j += 1

        processes = newProcesses[:]
        if (len(processes) == 0):
            break
        i += 1
    s = "time " + str(i) + "ms: Simulator ended (Contiguous -- Best-Fit)"
    print(s)


def bestLoc(dots, data, length):
    i = 0
    # print("starting best loc:")
    # print (data)
    # print(dots)
    smallest_loc = -1
    smallest_length = 256
    if len(dots) == 1:
        if data[dots[0]][2] - data[dots[0]][1] >= length:
            return dots[0]
        else:
            return (-1)
    elif (len(dots) == 0):
        return (-1)
    while i < len(dots):
        # print(dots[i])
        dstart = data[dots[i]][1]
        dend = data[dots[i]][2]
        if dend - dstart >= length and dend - dstart < smallest_length:
            smallest_length = dend - dstart
            smallest_loc = dots[i]

        i += 1
        # print("smallest_loc:", smallest_loc, "smallest_length:", smallest_length)
    return smallest_loc


def worstFitc(data, processes):
    print("time 0ms: Simulator started (Contiguous -- Worst-Fit)")
    i = 0
    hasArrivals = False
    hasExits = False
    while len(processes) > 0:
        # s = ""
        # for x in processes:
        # s = s + " " + str(x)
        # print("i:", str(i), s)
        arrivals, exits = arrival_endReady(processes, i, data)
        if len(arrivals) > 0:
            hasArrivals = True
        if len(exits) > 0:
            hasExits = True
        # print("i:", i, arrivals, exits)

        # if Process leaves at time i
        if (hasExits):
            for j in exits:
                s = "time " + str(
                    i) + "ms: Process " + data[j[1]][0] + " removed:"
                print(s)
                # print("i:", i, "Exit:", processes[j].name, processes[j].numMem)
                dstart = data[j[1]][1]
                dend = data[j[1]][2]
                data.pop(j[1])
                data.insert(j[1], [".", dstart, dend])
                # printData(data)
                mergeEverything(data)
                printData(data)
            hasExits = False

        # if Process arrives at time i
        if (hasArrivals):
            for j in arrivals:
                # print(data)
                isPlaced = False
                s = "time " + str(
                    i
                ) + "ms: Process " + processes[j].name + " arrived (requires " + str(
                    processes[j].numMem) + " frames)"
                print(s)
                length = processes[j].numMem
                dots = find_dot_loc(data)
                loc = worstLoc(dots, data, length)
                # print(dots)
                if loc >= 0:
                    isPlaced = True
                    dstart = data[loc][1]
                    dend = data[loc][2]
                    dlength = data[loc][2] - data[loc][1]
                    # print("here")
                    # print(data)
                    data.insert(loc,
                                [processes[j].name, dstart, dstart + length])
                    data.pop(loc + 1)
                    # printData(data)
                    if length < dlength:
                        data.insert(loc + 1, [".", dstart + length, dend])
                    if (data[loc][1] != dstart):  # THIS SHOULD BE UNNECESSARY
                        data.insert(loc, [".", dstart])
                    s1 = "time " + str(
                        i) + "ms: Placed process " + processes[j].name + ":"
                    print(s1)
                    printData(data)
                # unable to place process
                if (isPlaced is False):
                    if (length <= freeSpace(data)):
                        # enterDefragmentation
                        temp = defragmentation(data)
                        data = temp[0]
                        pList = temp[2]
                        defragValue = 186
                        s1 = "time " + str(
                            i
                        ) + "ms: Cannot place process " + processes[j].name + " -- starting defragmentation"
                        print(s1)
                        # # DEFRAG CODE HERE ##
                        i += defragValue
                        string = ''
                        l = 0
                        while (l < len(pList) - 1):
                            string += pList[l]
                            string += ', '
                            l += 1
                        string += pList[len(pList) - 1]
                        s1 = "time " + str(
                            i) + "ms: Defragmentation complete (moved " + str(
                                defragValue) + " frames: B, C, D, E)"
                        print(s1)
                        printData(data)
                        dots = find_dot_loc(data)
                        loc = bestLoc(dots, data, length)
                        if loc >= 0:
                            isPlaced = True
                            dstart = data[loc][1]
                            dend = data[loc][2]
                            dlength = data[loc][2] - data[loc][1]
                            # print("here")
                            # print(data)
                            data.insert(loc, [
                                processes[j].name, dstart, dstart + length
                            ])
                            data.pop(loc + 1)
                            # printData(data)
                            if length < dlength:
                                data.insert(loc + 1,
                                            [".", dstart + length, dend])
                            if (data[loc][1] !=
                                    dstart):  # THIS SHOULD BE UNNECESSARY
                                data.insert(loc, [".", dstart])

                            k = 0
                            while k < len(processes):
                                processes[k].start += defragValue
                                processes[k].stop += defragValue
                                k += 1

                            s1 = "time " + str(
                                i
                            ) + "ms: Placed process " + processes[j].name + ":"
                            print(s1)
                            printData(data)

                        # exits.append([j, -1])
                    else:
                        s1 = "time " + str(
                            i
                        ) + "ms: Cannot place process " + processes[j].name + " -- skipped!"
                        print(s1)
                        exits.append([j, -1])
                        # printData(data)
            hasArrivals = False

        newProcesses = []
        j = 0
        add = True
        while j < len(processes):
            add = True
            # print("time " + str(i) + "ms: Eliminating processes")
            '''
            print()
            s1 = ""
            for x in processes:
                    s1 += str(x) + "\n"
            print (s1)
            '''
            for exit in exits:
                if exit[0] == j:
                    add = False
                    # print("Removing loc", j, "in processes", processes[j])
            if (add):
                newProcesses.append(processes[j])
            j += 1

        processes = newProcesses[:]
        if (len(processes) == 0):
            break
        i += 1
    s = "time " + str(i) + "ms: Simulator ended (Contiguous -- Worst-Fit)"
    print(s)


def worstLoc(dots, data, length):
    i = 0
    # print("starting best loc:")
    # print (data)
    # print(dots)
    largest_loc = -1
    largest_length = 0
    if len(dots) == 1:
        if data[dots[0]][2] - data[dots[0]][1] >= length:
            return dots[0]
        else:
            return (-1)
    elif (len(dots) == 0):
        return (-1)
    while i < len(dots):
        # print(dots[i])
        dstart = data[dots[i]][1]
        dend = data[dots[i]][2]
        if dend - dstart >= length and dend - dstart > largest_length:
            largest_length = dend - dstart
            largest_loc = dots[i]
        i += 1
        # print("smallest_loc:", smallest_loc, "smallest_length:", smallest_length)
    return largest_loc


def contiguous(data, processes):
    # print(data)
    tempProc = []
    tempProc = createTemp(processes)
    # s1 = ""
    # for x in processes:
    # s1 += str(x) + "\n"
    # print (s1)
    nextFitc(data[:], tempProc)
    # rint(data)
    # or x in processes:
    # s1 += str(x) + "\n"
    # print (s1)
    print("")
    tempProc = createTemp(processes)
    bestFitc(data[:], tempProc)
    # print(data)
    # for x in processes:
    # s1 += str(x) + "\n"
    # print (s1)
    print("")
    tempProc = createTemp(processes)
    worstFitc(data[:], tempProc)
    print("")


def createTemp(processes):
    temp = []
    for p in processes:
        temp.append(Process(p.name, p.numMem, [p.start, p.stop - p.start]))
    return temp


def non_contiguous(data, processes):
    time = 0
    string = 'time '
    string += str(time)
    print('time ' + str(time) + 'ms: Simulator started (Non-contiguous)')
    inMemory = []
    while ((len(processes) > 0 or len(inMemory) > 0)):
        # will check for arrivals add them
        # to data and switch from process to inMem
        data = checkDone(data, inMemory, time)
        data = checkReady(processes, data, inMemory, time)
        time += 1
    print('time ' + str(time - 1) + 'ms: Simulator ended (Non-contiguous)')


def checkReady(processes, data, inMemory, time):
    i = 0
    end = len(processes)
    while (i < end):
        if (processes[i].start == time):
            print('time ' + str(time) + 'ms: Process ' + processes[i].name +
                  ' arrived (requires ' + str(processes[i].numMem) +
                  ' frames)')
            if (freeSpace(data) >= processes[i].numMem):
                data = nonContiguousAdd(data, processes[i], time)
                inMemory.append(processes[i])
                printData(data)
            else:
                print('time ' + str(time) + 'ms: Cannot place process ' +
                      processes[i].name + ' -- skipped!')

            processes.remove(processes[i])
            end -= 1
        else:
            i += 1
    return data


def checkDone(data, inMemory, time):
    i = 0
    end = len(inMemory)
    while (i < end):
        if ((inMemory[i].stop) == time):
            print('time ' + str(time) + 'ms: Process ' + inMemory[i].name +
                  ' removed:')
            data = deleteProcess(data, inMemory[i].name)
            inMemory.remove(inMemory[i])
            end -= 1
        else:
            i += 1
    return data


def nonContiguousAdd(data, process, time):
    i = 0
    left = process.numMem
    while (left):
        if (data[i][0] == '.'):
            sizeBlock = data[i][2] - data[i][1]
            if (sizeBlock > left):
                data = data[:i] + [[
                    process.name, data[i][1], data[i][1] + left
                ]] + data[i:]
                data[i + 1][1] = data[i][2]
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
    while (i < end):
        if (data[i][0] == name):
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
        if (lastEnd != element[1]):
            moved.append(element[0])
            wait += Len
        element[1] = lastEnd
        element[2] = element[1] + Len
        lastEnd = element[2]
    if ((lastEnd - 256) != 0):
        data.append(['.', lastEnd, 256])
    return [data, wait, moved]


def mergeEverything(data):
    i = 0
    end = len(data)
    while ((i + 1 != end)):
        if (data[i][0] == data[i + 1][0]):
            data[i][2] = data[i + 1][2]
            data.remove(data[i + 1])
            end -= 1
        else:
            i += 1


if __name__ == "__main__":
    # print('Init Data')
    data = initData()
    # printData(data)
    fileName = sys.argv[1]
    temp = parseFile(fileName)
    processes = temp[0]
    numProcess = temp[1]
    processes.sort(key=lambda x: x.start, reverse=False)
    '''
    for i in processes:
        print(i)
    print(data)
    '''
    # data = [["A", 2, 45], [".", 45, 75], ["B", 75, 100], [".", 100, 256] ]
    proc_cpy = []
    proc_cpy = createTemp(processes)
    contiguous(data, proc_cpy)
    proc_cpy = createTemp(processes)
    non_contiguous(data[:], proc_cpy)
