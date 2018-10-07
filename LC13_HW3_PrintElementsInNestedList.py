def main():
	print("Enter 1st list Elements")
	x=eval(input(""))
	print(x)
	printele(x)
	
def printele(x):
	for i in x:
		t=type(i)
		if t==list:
			printele(i)
		else:
			print(i,",")
		
if __name__=='__main__':
	main()