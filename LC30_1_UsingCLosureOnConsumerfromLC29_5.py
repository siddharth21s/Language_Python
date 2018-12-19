import random

def consume():
	while True:
		d1=yield 
		print("Recieved : ",d1)

def wraper(func):#closure for consume function
	def init():
		consumer = func()
		next(consumer)
		return consumer
	return init
		
def produce(consumer):
	while True:
		data = random.randint(1,100)
		consumer.send(data)
		print("Sent : ",data)
		yield 
		
def main():
	#consumer = consume()
	#consumer.send(None)# Or wecan use 'next(consumer)'
	#using wrapper to  call consume
	init_consumer = wraper(consume)
	consumer = init_consumer()
	producer = produce(consumer)
	for x in range(10):
		next(producer)
		
if __name__=="__main__":
	main()
