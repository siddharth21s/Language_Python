import copy
import io

def parseconfig(con_fig,format='='):
	res={}
	out={}
	fd= io.FileIO(con_fig)
	if fd!=None:
		while True:		#we can use (for line in fd) or (with open "")
			line=fd.readline()
			if line==b'':
				break
			line=str(line)
			if not (line.startswith("\\n") or line.startswith("b'#") ):
				
				k=line.lstrip("b'")
				k=k.rstrip('\\n\'')
				content=k.split("=")
				if len(content)>1:
					t=content[1].split(' #')
					content[1]=t[0]
				#r=copy.deepcopy(k)
				if not content[0]=='':
					print(content)
				if content[0]=='':
					continue
				elif len(content)>1:
					res[content[0]]=content[1]
					out[r]=res
				elif len(content)==1:
					r=content[0]
					out[r]=res
					res={}
		
		print(out)
		
		
def main():
	x=input("audio.conf:\t")
	parseconfig(x)
	
	
	
if __name__=='__main__':
	main()