def patt(n,j):
	#'''
	for i in range(1,n):
		for _ in range(n-i):
			print("\t",end="")
		for k in range(i-1,0,-1):
			print(str(j+k)+"\t",end="")
		for k in range(0,i,1):
			print(str(j+k)+"\t",end="")
		print()
	'''
	for i in range(1,n):
		for _ in range(n-i):
			print("\t",end="")
		for k in range(-n,n,1):
			if(k==-1 or k==0):
				pass
			elif(k<i):
				print((chr(ord(j)+abs(k)))+"\t",end="")
		print()
	'''
def main():
	x=eval(input("Enter number of rows:\t"))
	#y=input("Enter a char not string:\t")
	patt(x+1,1)
	
	
	
if __name__=="__main__":
	main()