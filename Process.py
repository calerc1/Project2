from __future__ import print_function

class Process:
	
	def __init__(self, Name, NumMem, Data):
		self.name = Name
		self.numMem = NumMem
		self.start = Data[0]
                self.stop = Data[1]

        def __str__ (self):
                return self.name + " " + self.numMem + " " + self.start + "-" + self.stop

