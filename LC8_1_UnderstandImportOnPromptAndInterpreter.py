def ADD(a,b):
	return a-b

def main():
	x,y=eval(input("Enter 2 numbers"))
	print("Result = %d" %ADD(x,y))

	
if __name__=='__main__': #this block is called boiler block
	print("Runningas standalone script",__name__)
	main()

else:
	print("Loaded as  Module",__name__)