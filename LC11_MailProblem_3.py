def FizzBuzz():
	for x in range(1,101):
		if x%3==0 and x%5==0:
			print('FizzBuzz')
		elif x%3==0:
			print('Fizz')
		elif x%5==0:
			print('Buzz')
		else:
			print(x)

def main():
	FizzBuzz()
	
if __name__=='__main__':
	main()