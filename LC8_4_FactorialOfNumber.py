def fact(n):
	if n<0:
		return "Does not exist"
	elif n<=1:
		return 1
	else:
		return n*fact(n-1)

def main():
	n=eval(input("Enter number"))
	print("Result",fact(n))
	
if __name__=='__main__':
	main()