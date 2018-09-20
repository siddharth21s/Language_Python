def digit(n):
	if n==0:
		return 0
	else:
		print(n%10)
		return digit(int(n/10))
	
def main():
	n=eval(input("Enter Digit\t"))
	digit(n)

	
if __name__=='__main__':
	main()
	