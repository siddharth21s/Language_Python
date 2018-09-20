def patt(n,j):
	for i in range(n,0,-1):
		for _ in range(n-i):
			print("\t",end="")
		for k in range(i-1,0,-1):
			print((chr(ord(j)+k))+"\t",end="")
		for k in range(0,i,1):
			print((chr(ord(j)+k))+"\t",end="")
		print()

def main():
	x=eval(input("Enter number of rows:\t"))
	y=input("Enter a char not string:\t")
	patt(x,y)
	
	
	
if __name__=="__main__":
	main()