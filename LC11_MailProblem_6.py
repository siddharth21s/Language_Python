def main():
	print("Enter string")
	x=input("")
	z=listcomp(x)
	print(z)
	
def listcomp(x):
	i=0
	y=''
	t=x[0]
	while i<len(x):
		if x[i]==' ':
			y=x[i+1]
			break
		i+=1
	if t==y:
		return True
	else:
		return False
	
if __name__=='__main__':
	main()