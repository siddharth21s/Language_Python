def fibo(n):
	s,i,j = 0,1,1
	print(i,j,end=" ")
	while(n>s):
		s=i+j
		i=j
		j=s
		if n>s:
			print(str(s),end=" ")

def main():
	x=eval(input("Enter number: "))
	fibo(x)

if __name__=="__main__":
	main()