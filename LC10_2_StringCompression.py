def compress(s):
	x,c,st=0,1,''
	#c=1
	#st=''
	while x<len(s):
		ch=s[x]
		while ((x+1)<len(s) and ch==s[x+1]):
			c=c+1
			x+=1
		if(c==1):
			st+=ch
		else:
			st+=ch+str(c)
		c=1
		x+=1
	return st
	
	
	''''while x<len(s):
		ch1=s[x]
		ch
	'''
	
	
def main():
	x=input("Enter string to compress:\t")
	print(compress(x))
	
	
if __name__=='__main__':
	main()