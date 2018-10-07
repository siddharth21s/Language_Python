def main():
	print("Enter string")
	x=input("")
	z=listcomp(x)
	print(z)
	
def listcomp(x):
	i=0
	z=''
	while i<len(x):
		if i==0 or i==3:
			z+=x[i].upper()
		else:
			z+=x[i]
		i+=1
	return z
	
if __name__=='__main__':
	main()