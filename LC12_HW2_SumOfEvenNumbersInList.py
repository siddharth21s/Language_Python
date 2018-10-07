def evesum(a):
	sum=0
	for i in a:
		if a[i]&1==0:
			sum+=a[i]
	return sum
def main():
	print("Enter list elements")
	y=[int(a) for a in input().split()]
	print("Result",evesum(y))
	
if __name__=='__main__':
	main()