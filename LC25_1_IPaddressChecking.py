
import re

def checkip(ip):
	pattern = re.compile("(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})")
	k=re.match(pattern,ip)
	type=k.group(1)
	print(type)
	type = int(type)
	if(int(k.group(2))<256 and int(k.group(3))<256 and int(k.group(4))<256):
		if(type<127 and type>0):
			print("Class A")
		elif(type<192 and type>127):
			print("Class B")
		elif(type<127 and type>192):
			print("Class C")
		elif(type<192 and type>224):
			print("Class D")
		elif(type<224 and type>256):
			print("Class E")
		else:
			print("Invalid IP")
	else:
		print("Invalid IP")
def main():
	ip=input("Enter IP:\t")
	checkip(ip)
	
	
if __name__=='__main__':
	main()
'''

try:
	n=10/0

except ZeroDivisionError as e:
	print(e,"222")

except Exception as e:
	print(e,"111")

'''