def patt(n,c):
	i=str(c)+"\t"
	for x in range(n,0,-1):
		print(i*x)
	
	
	
	
def main():
	x=eval(input("Enter number of rows\t"))
	y=input("Enter charater\t")
	patt(x,y)
	
	
	
if __name__=="__main__":
	main()