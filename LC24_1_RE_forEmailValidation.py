import re

def validate(exp):
	d=re.search("([a-zA-Z0-9.]+)@(\w.+)\.(\w+)$",exp)
	if d == None:
		return False
	else:
		print(d.group(0))
		return True


def main():
	x=input("Enter  Email:\t")
	res=validate(x)
	if res :
		print("Accepted")
	else:
		print("Not")
if __name__=="__main__":
	main()