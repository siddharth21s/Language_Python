def sum(n,s):
	if n==0:
		return 0
	else:
		s=n%10+sum(int(n/10),s)
		return s
	
def main():
	n=eval(input("Enter Digit\t"))
	print(sum(n,0))
	

	
if __name__=='__main__':
	main()
	