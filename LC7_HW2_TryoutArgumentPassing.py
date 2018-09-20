def variableargs(a,b,c,*d,**e):
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)
	
if __name__=='__main__':
	a,b,c=eval(input("Enter three numbers"))
	d=input("Enter a number or string")
	e='"name":"siddharth"'#not working, it is creates dictionary inside a dictionary
	variableargs(a,b+1,c,a,d,b,d=c,n=e)# d=c is also considered in **e dictionary
	print("2nd try")
	variableargs(a,b+1,c,d=c,n=e)# tuple is empty
	print("3rd try")
	variableargs(a,b+1,c<<1,d,e)# key value cant be expression error