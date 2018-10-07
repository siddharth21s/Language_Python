def fact(n):
	if n<0:
		return "Does not exist"
	elif n<=1:
		return 1
	else:
		return n*fact(n-1)

def special(n,s):
	if n==0:
		return 0
	else:
		s=fact(n%10)+special(int(n/10),s)
		return s
	
		
def main():
	n=eval(input("Enter number"))
	check=special(n,0)
	if check==n:
		print(n,"is a special number")
	else:
		print(n,"is not a special number")
	
if __name__=='__main__':
	main()