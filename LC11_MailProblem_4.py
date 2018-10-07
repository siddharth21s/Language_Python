def main():
	print("Enter string")
	x=input("")
	z=listcomp(x)
	print(z)
	
def listcomp(x):
	i=0
	z=[]
	z.append(x[0])
	while i<len(x):
		if x[i]==' ':
			z.append(x[i+1])
		i+=1
	return z
	
if __name__=='__main__':
	main()