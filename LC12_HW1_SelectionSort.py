def selection(l):
	i=0
	while i <= len(l):
		x=i
		while x < len(l):	
			temp = l[i]
			if ((x+1)< len(l)) and (temp > l[x+1]):
				l[i]=l[x+1]
				l[x+1]=temp
			x+=1
		i+=1
	return l
def main():
	x=eval(input("Enter List\t"))
	print(selection(x))
	
if __name__=='__main__':
	main()