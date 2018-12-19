def Verify(cls):
	def wrapper():
		manager_init = False
		manager_del = False
		for key in cls.__dict__:
			if key == "__init__":
				manager_init = True
			elif key == "__del__":
				manager_del = True
		if (not manager_del) or (not manager_init):
			raise NameError("Not having __init__ and/or __del__")
		else:
			print("constructor and destructor")
		return cls
	return wrapper
	
@Verify
class Test():
	def __init__():
		pass
	def __del__():
		pass
		
t = Test()

@Verify
class Tes():
	def __init__():
		pass

t = Tes()