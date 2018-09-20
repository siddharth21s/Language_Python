def patt(n):
	i="*\t"
	for x in range(0,n+1,1):
		print(i*x)
	'''	
	for i in range(1,n):
		for _ in range(0,i,1):
			print("*\t",end="")
		print("")

	'''
	
	
def main():
	x=eval(input("Enter number of rows"))
	patt(x)
	
	
	
if __name__=="__main__":
	main()