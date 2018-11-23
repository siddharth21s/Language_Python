import re

def validate(exp):
	return re.sub(r"\d","",exp)

def main():
	x=input("Enter Expression:\t")
	res=validate(x)
	print(res)
if __name__=="__main__":
	main()