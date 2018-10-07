def main():
	print("Enter List")
	x=eval(input(""))
	z=listcomp(x)
	print(z)
	
def listcomp(x):
	i=0
	while i<len(x):
		if x[i]==3 and x[i+1]==3:
			return False
		i+=1
	return True
	
if __name__=='__main__':
	main()