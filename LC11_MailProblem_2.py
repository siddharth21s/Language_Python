def repEven(s):
	x,c,st,ct=0,1,'',' '
	#c=1
	#st=''
	while x<len(s):
		ch=s[x]
		#if ch=='s' or ch=='S':	
		while ((x+1)<len(s) and ct!=s[x]):
			#st+=s[x]
			c=c+1
			x+=1
		if (c+1)%2==0:
			st+='EVEN '
		else:
			st+='ODD '
		'''else:
			while((x+1)<len(s) and ct!=s[x]):
				x+=1'''
		c=1
		x+=1
	return st
	
	
	''''while x<len(s):
		ch1=s[x]
		ch
	'''
	
	
def main():
	x=input("Enter string to compress:\t")
	print(repEven(x))
	
	
if __name__=='__main__':
	main()