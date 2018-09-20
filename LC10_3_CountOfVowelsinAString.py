def vowel(s):
	'''x=0
	b=len(s)
	for i in range(0,b,1):
		c=s[i]
		'''
		
	v='aeiouAEIOU'
	c=0
	for x in s:
		if x in v:
			c+=1
	return c
	
		
	'''
		if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):
			x+=1
	return x'''
	
def main():
	x=input("Enter a string")
	print("number of vowels:",vowel(x))
	
if __name__=='__main__':
	main()