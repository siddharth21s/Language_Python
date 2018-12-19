
# generators using lambda
def  gen(x):
	return lambda n:n+x
	
gen_c = gen(10)
print(gen_c(1))

gen_d = gen(5)
print(gen_d(10))

print("\n***Map***\n")

# map
# gettting lenght of all lines in a files

fd=open("test1.txt")
l = fd.readlines()

c=map(lambda x:len(x), l)

for m in c:
	print(m)
fd.close()	
print("*******")

#getting word count on all the 

fd = open("test1.txt")
l = fd.readlines()

c = map(lambda x:len(x.split(" ")),l)

for m in c:
	print(m)
c = map(lambda x:len(x.split(" ")),l)
fd.close()	

# filter
# 

print("---Filter----")
h=[10,20,30,1,2,3]

d= filter(lambda x:x>10,h)

for m in d:
	print(m)
	
	
print("-----Reduce---")

# Reduce
import functools as fc
d = fc.reduce(lambda x,y:x*y, range(1,10))
print(d)
