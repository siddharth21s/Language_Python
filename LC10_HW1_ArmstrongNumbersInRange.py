def sum(n,s):
	if n==0:
		return 0
	else:
		s=(n%10)**3+sum(int(n/10),s)
		return s
	

def armstrong(n):
	check=sum(n,0)
	if n==check:
		print(n)

	
def main():
	x=eval(input("Enter lower bound:\t"))
	y=eval(input("Enter upper bound:\t"))
	print("Prime numbers are:")
	for i in range(x,y+1,1):
		armstrong(i)
		
if __name__=='__main__':
	main()