def main():
	print("Enter 1st list Elements")
	x=eval(input(""))
	print(x)
	findtype(x)
	
def findtype(x):
	for i in x:
		t=type(i)
		print(t)
		
if __name__=='__main__':
	main()