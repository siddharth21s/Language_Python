x = input("Enter a 1st string \t")

def repl(x):
	u = x.rfind('not')
	v = x.rfind('bad')
	#print(u,v)
	x = x.replace('not ','')
	x = x.replace('bad','good')
	print(x)
	
repl(x)