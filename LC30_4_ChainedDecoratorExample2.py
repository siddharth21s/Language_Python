import time

def LogDec(func):
	def log(args):
		return func(str(time.time())+' '+args)
	return log
	
def LogName(func):
	def log(args):
		return func("Sid: "+args)
	return log
	
@LogDec
@LogName

def Logger(data):
	print("Logged: ",data)
	
def main():
	Logger("BasketBall")
	time.sleep(2)
	Logger("Football")
	
if __name__=="__main__":
	main()