class Process:
    def __init__(self, Name, NumMem, Data):
        self.name = Name
        self.numMem = int(NumMem)
        self.start = int(Data[0])
        self.stop = int(Data[0]) + int(Data[1])

    def __str__(self):
        return self.name + " " + str(self.numMem) + " " + str(self.start)
        + " " + str(self.stop)
