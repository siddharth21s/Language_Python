def patt(n):
	i,j="\t*","\t"
	for x in range(-n,n+1):
		if x<0:
			print(j*(abs(x)),i*(n-abs(x)))
		elif x==0:
			print(i*(2*n-1))
		else:
			print(j*(n-1),i*(n-abs(x)))
	
def main():
	x=eval(input("Enter number of rows"))
	patt(x)
	
if __name__=="__main__":
	main()