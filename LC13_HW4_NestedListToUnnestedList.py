def main():
	print("Enter 1st list Elements")
	x=eval(input(""))
	print("x: ",x)
	z=[]
	z=printele(x,z)
	print("Result: ",z)
	
	
def printele(x,z):
	for i in x:
		t=type(i)
		if t==list:
			printele(i,z)
		else:
			z.append(i)
	return z	
if __name__=='__main__':
	main()