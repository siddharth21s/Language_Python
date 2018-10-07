def main():
	print("Enter string")
	x=input("")
	z=eveodd(x)
	print(z)
	
def eveodd(x):
	i=0
	u=x.upper()
	l=x.lower()
	f=''
	while i<len(x):
		if i%2==0:
			f+=u[i]
		else:
			f+=l[i]
		i+=1
	return f
	
if __name__=='__main__':
	main()