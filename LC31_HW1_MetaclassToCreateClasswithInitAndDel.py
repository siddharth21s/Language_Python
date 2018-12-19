def init(self):
	pass

def des(self):
	pass
	
	
class DebugM(type):
	def __init__(self,names,bases,member_dict):
		#print(self)
		manager_init = False
		manager_del = False
		for key in self.__dict__:
			if key == "__init__":
				manager_init = True
			elif key == "__del__":
				manager_del = True
		if (not manager_del) or (not manager_init):
			print("ADDED")
			setattr(self,'__init__',init)
			setattr(self,'__del__',des)
			return type.__init__(self,names,bases,member_dict)#,{'__init__':init,'__del__':des})
		else:
			print("PARSED")
			return type.__init__(self,names,bases,member_dict)

	
class BaseM(metaclass = DebugM):
	pass

class DerivedM(BaseM):
	def __init__():
		pass
	def __del__():
		pass
	
print([x for x in DerivedM.__dict__])
print([x for x in BaseM.__dict__])