import re

def Generator(pattern,file):
	fd = open(file)
	pat = re.compile(pattern)
	
	for line in fd:
		if pat.search(line):
			yield line
	fd.close()
	
	
def main():
	file = "audio.conf"
	x=Generator("\A#", file)
	
	for _ in range(10):
		print(next(x))
		
if __name__ == "__main__":
	main()
	