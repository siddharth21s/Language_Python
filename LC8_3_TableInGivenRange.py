def table(l,u):
	for x in range(l,u+1,1):
		print("Table for :" ,x)
		for y in range(1,11,1):
			print(x,"x",y,"=",x*y)
		
def main():
	l,u=eval(input("Enter lower bound and Upper bound"))
	table(l,u)
	
if __name__=='__main__':
	main()