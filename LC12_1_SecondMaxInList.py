def secmax(l):
	max,smax=l[0],l[1]
	for x in range(0,len(l)):
		if l[x] < max and l[x]>smax:
			smax=l[x]
		elif (l[x] > max) and (l[x]>smax):
			smax=max
			max=l[x]
	return [max,smax]

def main():
	x=eval(input("Enter List"))
	print(secmax(x))
	
if __name__=='__main__':
	main()