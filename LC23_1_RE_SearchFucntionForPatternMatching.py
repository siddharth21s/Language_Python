import re
def find(patt,string):
	v=0
	j=0
	while j<len(string):
		m= re.search(patt,string[v:])
		if (m == None):
			break
		else:
			print(v+m.start(),v+m.end())
			v+=m.end()
		j+=len(patt)

def main():
	x=input("Enter pattern : ")
	y=input("Enter string: ")
	find(x,y)
	
	
if __name__=="__main__":
	main()