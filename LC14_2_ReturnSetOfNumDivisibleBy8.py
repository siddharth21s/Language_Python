def retset(x):
	z=set([])
	for i in x:
		if i&7==0:
			z.add(i)
	return z

def main():
	print("Enter 1st list Elements")
	x=eval(input(""))
	print("x: ",x)
	z=retset(x)
	print("Result: ",z)
	
	

if __name__=='__main__':
	main()