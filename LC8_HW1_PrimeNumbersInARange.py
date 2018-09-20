def prime(l,u):
	for x in range(l,u+1,1):
		if x<1:
				continue
		elif x<=2:
				print(x)
		else:
			for n in range(2,x,1):
				if((x%n)==0):
					#print(x,"is not prime")
					break
				elif(n==x-1):
					print(x)

def main():
	x=eval(input("Enter lower:\t"))
	y=eval(input("Enter upper:\t"))
	print("Lower :",x,"Upper :",y)
	print("Prime Numbers in the given range are")
	prime(x,y)
	
if __name__=='__main__':
	main()