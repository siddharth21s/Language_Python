class A:
	def m(self):
		print("Class A's m")
	def n(self):
		print("Class A's n")
	
class  B(A):
	def l(self):
		print("Class B's l")
		
class C(A):
	def m(self):
		print("Class C's m")
		
class D(B,C):
	pass
	
def main():
	o = A()
	o.m()
	b = B()
	b.l()
	j = C()
	j.m()
	e = D()
	e.m()
	e.l()
	e.n()
	A.m(e)

	
if __name__=='__main__':
	main()