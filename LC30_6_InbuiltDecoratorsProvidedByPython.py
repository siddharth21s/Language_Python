#class methods and staticmethods are provided by python inbuilt


class Test(object):
	@classmethod
	def Display(cls):
		print(id(cls))
		print("Display")
		
	@staticmethod
	def Foo():
		print("Static Called")
		
	def Instanci(self):
		print("Instanciated")
		
def main():
	c=Test()
	c.Display()
	Test.Display()
	c.Foo()
	Test.Foo()
	c.Instanci()
	Test.Instanci(c)
	
if __name__=="__main__":
	main()