import copy
def main():
	print("Enter Dictionary keys list Elements")
	x=[int(a) for a in input().split()]
	x=dict.fromkeys(x)
	print("x: ",x)
	print("Enter Values to be added")
	y=[int(a) for a in input().split()]
	print("y: ",y)
	z= copy.deepcopy(x)
	z=from_keys(z,y)
	print(z)
	i=4
	while True:
		i=input("\n 1.update\n2.append\n3.delete\n4.search\n5.display all\nEnter your choice \t:")
		if i in '1':
			update(z)
		elif i in '2':
			appendz(z)
		elif i in '3':
			delete(z)
		elif i in '4':
			search(z)
		elif i in '5':
			display(z)
		else:
			break
	
def update(z):
	x=eval(input("Enter key:\t"))
	y=eval(input("Enter value:\t"))
	z[x]=y
	print(z)
	return
	
def appendz(z):
	x=eval(input("Enter key:\t"))
	y=eval(input("Enter value:\t"))
	if x in z:
		if type(z[x])==int :
			t=[z[x]]
			t.append(y)
			z[x]=t
		else:
			t=[]
			t=z[x]
			t.append(y)
			z[x]=t
		print(z)
	return
	
def delete(z):
	x=eval(input("Enter key:\t"))
	y=eval(input("Enter value:\t"))
	if (x in z ):
		if type(z[x]) == list and y in z[x] and len(z[x])>1:
			z[x].remove(y)
			print("in",z[x])
		if type(z[x])==list and len(z[x])==1:
			t=z[x]
			z[x]=t[0]
		else:
			z.pop(x)
		print(z)
	else:
		print("Element not found")
	return
	
def search(z):
	x=eval(input("Enter key:\t"))
	y=eval(input("Enter value:\t"))
	if (x in z )and(z[x]==y):
		print("Element found")
	else:
		print("not found")
	return
	
def display(z):
	for i in z:
		if type(z[i])==list:
			for x in z[i]:
				print(i,":",x)
		else:
			print(i,":",z[i])
	return
	
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