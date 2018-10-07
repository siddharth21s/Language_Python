def packetize(flag,crc,rev,lenght,data):
	pack=0
	pack=flag&3
	pack=pack<<5
	pack=pack|(crc&((1<<5)-1))
	pack=pack<<3
	pack=pack|(rev&((1<<3)-1))
	pack=pack<<9
	pack=pack|(lenght&((1<<9)-1))
	pack=pack<<13
	pack=pack|(data&((1<<13)-1))
	return pack
	
def depacketize(pack):
	data=pack&((1<<13)-1)
	print("Data: ",data)
	pack=pack>>13
	lenght=pack&((1<<9)-1)
	print("Lenght: ",lenght)
	pack=pack>>9
	rev=pack&((1<<3)-1)
	print("Reserved: ",rev)
	pack=pack>>3
	crc=pack&((1<<5)-1)
	print("CRC: ",crc)
	pack=pack>>5
	flag=pack&3
	print("Flag: ",flag)
	return 0

def main():
	x=eval(input("Enter flag value 2 bit: "))
	print(bin(x))
	y=eval(input("Enter CRC value 5 bits: "))
	print(bin(y))
	u=eval(input("Enter reserved value 3 bits: "))
	print(bin(u))
	z=eval(input("Enter lenght value 9 bits: "))
	print(bin(y))
	w=eval(input("Enter data value 13 bits: "))
	print(bin(w))
	n=packetize(x,y,u,z,w)
	print('Packet:',n)
	print(bin(n))
	depacketize(n)
	
	
if __name__=='__main__':
	main()