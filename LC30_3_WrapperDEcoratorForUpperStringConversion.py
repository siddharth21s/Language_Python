

def wraper(func):#closure for consume function
	def init():
		consumer = func()
		next(consumer)
		return consumer
	return init
	
@wraper
def ToUpper():
	while True:
		d1=yield 
		d1 = str(d1)
		print("Converted : ",d1.upper())
		
def start(consumer):
	while True:
		data = input("Enter string:\t")
		if data in "ENDendEnd":
			return
		consumer.send(data)
		print("Sent : ",data)
		yield 
		
def main():
	#using wrapper as decorator
	Upper = ToUpper()
	#consumer.send(None)# Or wecan use 'next(consumer)'
	
	Starter = start(Upper)
	while True:
		try:
			next(Starter)
		except StopIteration:
			break
		
if __name__=="__main__":
	main()