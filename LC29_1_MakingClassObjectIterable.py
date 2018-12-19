class Autogernerate():
	def __init__(self,start,end,step=1):
		self.start = start
		self.end = end
		self.step = step
		
	'''
	def next(self):
		self.start+=self.step
		if self.start >=self.end:
			raise StopIteration
		return self.start
	'''
	def __next__(self):
		#return self.next()
		self.start+=self.step
		if self.start >=self.end:
			raise StopIteration
		return self.start
		
	def __iter__(self):
		return self
		
		
def  main():
	x=Autogernerate(0,20,5)
	for i in x:
		print(i)
		
if __name__=="__main__":
	main()