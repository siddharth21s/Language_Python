def table(l,u):
	for x in range(l,u+1,1):
		print("Table for: ",x)
		for i in range(1,11,1):
			print(x,"x",i,"=",x*i)
	
def main():
	x=eval(input("Enter Lower bound"))
	y=eval(input("Enter Lower bound"))
	table(x,y)
	
if __name__=='__main__':
	main()