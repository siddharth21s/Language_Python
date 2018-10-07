import copy
def main():
	print("Enter Dictionary keys list Elements")
	x=[str(a) for a in input().split()]
	x=dict.fromkeys(x)
	print("x: ",x)
	print("Enter Values to be added")
	y=[str(a) for a in input().split()]
	print("y: ",y)
	z= copy.deepcopy(x)
	z=from_keys(z,y)
	print("Result: ",z)
	print("Original: ",x)
	
def from_keys(x,y):
	if len(y)==1:
		for i in x:
			x[i]=y[0]
	else:
		t=len(y)
		j=0
		for i in x:
			x[i]=y[j]
			j+=1
			if(j==t):
				break
	return x
			
			
if __name__=='__main__':
	main()