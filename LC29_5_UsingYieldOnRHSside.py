import random

def consume():
	while True:
		d1=yield 
		print("Recieved : ",d1)

def produce(consumer):
	while True:
		data = random.randint(1,100)
		consumer.send(data)
		print("Sent : ",data)
		yield 
		
def main():
	consumer = consume()
	consumer.send(None)# explicitly calling
	producer = produce(consumer)
	for x in range(10):
		next(producer)
		
if __name__=="__main__":
	main()
		
	
	