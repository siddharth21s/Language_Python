def patt(n):
	i,j="\t*","\t"
	for d in range(n,0,-1):
		if n!=d:
			print(i*d,j*(2*(n-d)-1),i*d)
		else:
			print(i*(2*n-1))
	
def main():
	x=eval(input("Enter a number"))
	patt(x)
	
if __name__=="__main__":
	main()