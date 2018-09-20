def patt(n,c):
	i=str(c)+"\t"
	j="\t"
	for x in range(n,0,-1):
		print(str(j*(n-x))+str(i*x))
'''	
	for i in range(n,0,-1):
		for _ in range(n-i):
			print("\t",end="")
		for _ in range(i):
			print("*\t",end="")
		print()
			
		
	
	
	'''
def main():
	x=eval(input("Enter number of rows"))
	y=input("Enter charater\t")
	patt(x+1,y)
	
	
	
if __name__=="__main__":
	main()