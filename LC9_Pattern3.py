def patt(n):
	i="*\t"
	for x in range(n,0,-1):
		print(i*x)
	
	
	
	
def main():
	x=eval(input("Enter number of rows"))
	patt(x)
	
	
	
if __name__=="__main__":
	main()