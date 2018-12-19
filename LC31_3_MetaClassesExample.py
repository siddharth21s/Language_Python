def debugmethod(cls):
    print("debug method invoked")
    return cls
'''
@debugmethod
class Base(object):
    pass

class Derived(Base):
    pass
'''
class DebugM(type):
	def __init__(self,names,bases,member_dict):
		print("Debug Invoked")
		return type.__init__(self,names,bases,member_dict)

#@debugmethod		
class BaseM(metaclass = DebugM):
	pass
	
class DerivedM(BaseM):
	pass
	
c = DerivedM()
