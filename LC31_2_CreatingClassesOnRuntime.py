def Add(self):
	return self.no1+self.no2
	
def Mul(self):
	return self.no1*self.no2
	
def init(self,a,b):
	self.no1 = a 
	self.no2 = b
	
def main():
	A = type('A', (object,),{'__init__':init,'Add':Add,'Mul': Mul})
	obj = A(10,20)
	print(obj.Add())
	print(obj.Mul())
	print([x for x in A.__dict__])
	
if  __name__ == "__main__":
	main()