
def Isprime(x):
	if x<1:
			return False
	elif x<=2:
			return True
	else:
		for n in range(2,x,1):
			if((x%n)==0):
				return False
			elif(n==x-1):
				return True
				
				
def PrimeGenerator(start,end,step=1):
	for num in range(start,end+1,step):
		if Isprime(num):
			yield num

def main():
	st = eval(input("Enter start:\t"))
	en = eval(input("Enter end:\t"))
	sp = eval(input("Enter step:\t"))
	
	x = PrimeGenerator(st,en,sp)
	for _ in x:
		print(next(x))
		
if __name__=="__main__":
	main()