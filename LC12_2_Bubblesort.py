def bubble(l):
	i=0
	while (i+1) < len(l):
		x=0
		while x+1 < len(l)-i:	
			temp=l[x]
			if temp > l[x+1]:
				l[x]=l[x+1]
				l[x+1]=temp
			x+=1
		i+=1
	return l
def main():
	x=eval(input("Enter List\t"))
	print(bubble(x))
	
if __name__=='__main__':
	main()