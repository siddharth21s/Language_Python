def FuncDecOnClass(cls):
	cls.added_aatribute = "Decorated Attirbute"
	cls.empty_list=[]
	return cls
	
@FuncDecOnClass
class Temp(object):
	def __init__(self):
		self.acc_no=1
	def Display(self):
		pass
		
@FuncDecOnClass
class Test(object):
	def __init__(self):
		self.id=1
		
def main():
	print(Temp.__dict__)
	print(Test.__dict__)
	t= Temp()
	print(t.__dict__)
	
if __name__=="__main__":
	main()