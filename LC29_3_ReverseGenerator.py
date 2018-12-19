
class ForwardReverseGenerator():
	def __init__(self,start):
		self.start=start
	
	def ___iter__(self):
		start = 1
		while start <= self.start:
			yield start
		start -=1
		
	def __reversed__(self):
		start = 0
		while start >= self.start:
			yield start
		start +=1
		
	
def main():
	
	x = ForwardReverseGenerator(10)
	
	for i in x:
		print(i)
		
	for i in reversed(x):
		print(i)
		
if __name__ =="__main__":
	main()