def patt(n):
	i,j='\t*','\t'
	for x in range(-n,n+1):
		print(j*abs(x),i*(2*(n-abs(x))-1))
	
def main():
	x=eval(input("Enter number of rows"))
	patt(x)
	
if __name__=='__main__':
	main()