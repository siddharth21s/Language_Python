def main():
	print("Enter string")
	x=input("")
	z=listcomp(x)
	print(z)
	
def listcomp(x):
	i=0
	z=''
	while i<len(x):
		z+=3*x[i]
		i+=1
	return z
	
if __name__=='__main__':
	main()