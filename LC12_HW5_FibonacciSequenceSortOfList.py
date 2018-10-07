def fibo(n):
	s,i,j = 0,1,1
	fiblis=[0,1,1]
	while(n>s):
		s=i+j
		i=j
		j=s
		fiblis.append(s)
	return fiblis
	
def max(l):
	m=l[0]
	
	for x in range(0,len(l)):
		if len(l)>x+1 and l[x+1] > m:
			m=l[x+1]
	return m

def check(l):
	m=max(l)
	fib=fibo(m)
	res=[]
	for x in l:
		if (x in fib):
			res.append(x)
	return res

	
def main():
	print("Enter list Elements")
	y=[int(a) for a in input().split()]
	print(sorted(check(y)))
	
if __name__=='__main__':
	main()