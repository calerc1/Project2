from __future__ import print_function

class Process:
	
	def __init__(self, Name, NumMem, Data):
		self.name = Name
		self.numMem = NumMem
		self.data = Data
	
	def __str__(self):
		return self.name + " " +   self.numMem + " " +  str(self.data)
