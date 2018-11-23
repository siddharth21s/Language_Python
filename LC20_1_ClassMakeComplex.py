class Complex:
	def __init__(self,real=0,imagi=0):
		self.real=real
		self.imagi=imagi
	def __repr__(self):
		if (self.imagi <0):
			print(str(self.real)+str(self.imagi)+'i')
		else:
			print(str(self.real)+'+'+str(self.imagi)+'i')
	def __del__(self):
		print("Destructed")
	def __add__(self,obj):
		if isinstance(obj,int):
			self.real+=obj
		else:
			print(str(self.real+obj.real)+"+"+str(self.imagi+obj.imagi)+'i')
	def __sub__(self,obj):
		if (self.imagi-obj.imagi)>0:
			print(str(self.real-obj.real)+"+"+str(self.imagi-obj.imagi)+"i")
		else:
			print(str(self.real-obj.real)+str(self.imagi-obj.imagi)+"i")
	def __gt__(self,obj):
		if ((self.real>obj.real) and (self.imagi>obj.imagi)):
			return True
		else:
			return False
	def __ge__(self,obj):
		if ((self.real>=obj.real) and (self.imagi>=obj.imagi)):
			return True
		else:
			return False
	def __le__(self,obj):
		if ((self.real<=obj.real) and (self.imagi<=obj.imagi)):
			return True
		else:
			return False
	def __lt__(self,obj):
		if ((self.real<obj.real) and (self.imagi<obj.imagi)):
			return True
		else:
			return False
	def __eq__(self,obj):
		if ((self.real==obj.real) and (self.imagi==obj.imagi)):
			return True
		else:
			return False
	def __mul__(self,obj):
		return str(self.real*obj.real)+"+"+str(self.imagi*obj.imagi)+"i"
			
def main():
	c=Complex(3,2)
	c.__repr__()
	d=Complex(5,6)
	d.__repr__()
	print(c>d)
	print(d>c)
	print(c>=d)
	print(d>=c)
	print(c<d)
	print(d<c)
	print(c<=d)
	print(d<=c)
	print(c==d)
	print(c*d)
	c+d
	c-d
	c+9
	c.__repr__()
	
	
if __name__=='__main__':
	main()