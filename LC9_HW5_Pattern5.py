def patt(n,c):
	i=str(c)+"\t"
	j="\t"
	for x in range(1,n,1):
		print(str(j*(n-x))+str(i*x)+str(i*(x-1)))

def main():
	x=eval(input("Enter number of rows"))
	y=input("Enter charater\t")
	patt(x+1,y)
	
	
if __name__=="__main__":
	main()