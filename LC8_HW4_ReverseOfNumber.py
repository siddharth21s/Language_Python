def digit(n):
	s=0
	while(n!=0):
		s=s*10+n%10
		n=int(n/10)
	return s
	
def main():
	n=eval(input("Enter Digit\t"))
	print(digit(n))

	
if __name__=='__main__':
	main()
	