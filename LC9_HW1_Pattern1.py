def patt(n,c):
	i=str(c)+"\t"
	for x in range(0,n+1,1):
		print(i*x)

def main():
	x=eval(input("Enter number of rows\t"))
	y=input("Enter charater\t")
	patt(x,y)
	
	
	
if __name__=="__main__":
	main()