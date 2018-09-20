def slice(x,st,end,step=1):# default value for step count is 1
	return x[st:end:step]
	
print(slice("Siddharth",3,5))
print(slice("Siddharth",1,7,2))