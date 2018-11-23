import copy
import io

def parseconfig(x,y,z):
	i=0
	f=0
	res=''
	f=open("res.txt","w")
	f1= io.FileIO(x)
	f2= io.FileIO(y)
	f3= io.FileIO(z)
	if f1!=None and f2!=None and f3!=None:
		
		while True:		#we can use (for line in fd) or (with open "")
			l1=f1.readline()
			l2=f2.readline()
			l3=f3.readline()
			if l1==b'' or l2==b'' or l3==b'':
				break
			l1=str(l1)
			l2=str(l2)
			l3=str(l3)
			print(l1,l2,l3)
			#if not ((l1.startswith("\\n") or l1.startswith("b'#") ) and l2.startswith("\\n") or l2.startswith("b'#") and l3.startswith("\\n") or l3.startswith("b'#")):	
			k=l1.lstrip("b'")
			k=k.rstrip('\\r\\n\'')
			m=l2.lstrip("b'")
			m=m.rstrip('\\r\\n\'')
			n=l3.lstrip("b'")
			n=n.rstrip('\\r\\n\'')
			res=k+':'+m+':'+n+';'
			print(k,m,n)
			f.write(res)
		print()
		
def main():
	x=input("1.txt:\t")
	y=input("2.txt:\t")
	z=input("3.txt:\t")
	parseconfig(x,y,z)
	
	
	
if __name__=='__main__':
	main()