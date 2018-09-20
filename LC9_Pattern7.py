def patt(n,j):
	for i in range(1,n):
		for k in range(0,i,1):
			print((chr(ord(j)+k))+"\t",end="")
		print("")
		
		
def main():
	x=eval(input("Enter number of rows:\t"))
	y=input("Enter a char not string:\t")
	patt(x,y)
	
	
	
if __name__=="__main__":
	main()