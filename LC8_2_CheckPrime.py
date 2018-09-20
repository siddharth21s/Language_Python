def prime(x):
	if x<1:
			print(x,"is not prime")
	elif x<=2:
			print(x,"is prime")
	else:
		for n in range(2,x,1):
			if((x%n)==0):
				print(x,"is not prime")
				break
			elif(n==x-1):
				print(x,"is prime")

def main():
	x=eval(input("Enter number"))
	print("Entered Number :",x)
	prime(x)
	
if __name__=='__main__':
	main()