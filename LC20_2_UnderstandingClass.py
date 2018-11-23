class Human:
	country='India'
	def __init__(self,name,address,aadharno):
		self.name=name
		self.address=address
		self.aadharno=aadharno
		print("Constructor invoked for %s" %name)
	def __del__(self):
		print("Destruction of %s"%self.name)
	def getName(self):
		return self.name
	def setName(self, n):
		self.name=n

def main():
	s1=Human("Siddharth","168,MG Road",1275)
	s1.getName()
	print(s1.name)
	s1.setName("Sid")
	print(s1.__dict__)
	print(s1.country)
	print(s1.__dict__)
	print(Human.__dict__)
	Human.country='Greenland'
	print(Human.country)
	print(s1.__dict__)
	print(s1.country)
	print(Human.__dict__)
	
if __name__=='__main__':
	main()