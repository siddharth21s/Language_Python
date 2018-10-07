def prime(x):
	if x>0 and x<=2:
			return x
	else:
		for n in range(2,x,1):
			if((x%n)==0):
				#print(x,"is not prime")
				return 0
			elif(n==x-1):
				return x
	return 0

def main():
	print("Enter list Elements")
	y=[int(a) for a in input().split()]
	z=[]
	for x in y:
		if(prime(x)!=0):
			z.append(x)
	print(z)
	
if __name__=='__main__':
	main()