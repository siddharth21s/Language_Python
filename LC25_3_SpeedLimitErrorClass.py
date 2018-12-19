class SpeedError(Exception):
	def __init__(self,speed):
		self.speed=speed
	def __str__(self):
		return "Speed is "+str(self.speed)
		
class AboveLimit(SpeedError):
	def __init__(self,speed):
		SpeedError.__init__(self,speed)
	
class BelowLimit(SpeedError):
	def __init__(self,speed):
		SpeedError.__init__(self,speed)
	
def main():
	while True:
		try:
			speed = eval(input("Enter Speed"))
			if speed>80:
				x = AboveLimit(speed)
				raise x
			elif speed<20:
				raise BelowLimit(speed)
			else:
				print("Speed In limit")
				break
		except AboveLimit as e:
			print(e,"is AboveLimit")
		
		except BelowLimit as e:
			print(e,"is BelowLimit")
		
		finally:
			print("COOL")
		
if __name__=="__main__":
	main()