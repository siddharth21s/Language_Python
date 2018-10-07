def packetize(flag,crc,lenght,data):
	pack=0
	pack=flag&1
	pack=pack<<7
	pack=pack|(crc&127)
	pack=pack<<9
	pack=pack|(lenght&511)
	pack=pack<<15
	pack=pack|(data&((2**15)-1))
	return pack
	
def depacketize(pack):
	data=pack&(2**15-1)
	print("Data: ",data)
	pack=pack>>15
	lenght=pack&511
	print("Lenght: ",lenght)
	pack=pack>>9
	crc=pack&127
	print("CRC: ",crc)
	pack=pack>>7
	flag=pack&1
	print("Flag: ",flag)
	return 0

def main():
	x=eval(input("Enter flag value 1 bit: "))
	print(bin(x))
	y=eval(input("Enter CRC value 7 bits: "))
	print(bin(y))
	z=eval(input("Enter lenght value 9 bits: "))
	print(bin(y))
	w=eval(input("Enter data value 15 bits: "))
	print(bin(w))
	n=packetize(x,y,z,w)
	print('Packet:',n)
	print(bin(n))
	depacketize(n)
	
	
if __name__=='__main__':
	main()