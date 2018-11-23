import copy
def main():
	print("Enter 1st Dictionary:\t")
	x=eval(input(""))
	print("x: ",x)
	x=dict.fromkeys(x)
	print("Enter 2nd Dictionary:\t")
	y=eval(input(""))
	print("y: ",y)
	z= copy.deepcopy(x)
	z=from_keys(z,y)
	print("Result: ",z)
	
def from_keys(x,y):
	p=[]
	for h in y:
		p.append(y[h])
	print(p)
	if len(y)==1:
		for i in x:
			x[i]=y[0]
	else:
		t=len(p)
		j=0
		for i in x:
			x[i]=p[j]
			j+=1
			if(j==t):
				break
	return x
			
			
if __name__=='__main__':
	main()