def sum(n,s):
	if n==0:
		return 0
	else:
		s=(n%10)**3+sum(int(n/10),s)
		return s
	
def main():
	n=eval(input("Enter Digit\t"))
	s=sum(n,0)
	if(n==s):
		print(n,"Is an armstrong number")
	else:
		print(n,"is not an armstrong number")
	

	
if __name__=='__main__':
	main()
	