import threading as th
import time

data=0
threads=[]
lock=th.Lock()

def getjob():
	global data
	lock.acquire()
	data+=1
	x=data
	lock.release()
	return x
	
def processjob():
	print(getjob())
	
if __name__=="__main__":
	#t = th.Thread(target = worker)
	#t.setDaemon(True)#to make a daemon process
	#t.start()
	#t.join()#not returning control until the thread is done processing
	
	for i in range(10):
		t=th.Thread(target = processjob)
		threads.append(t)
		print("thread %d Started"%i)
		
	for y,o in enumerate(threads):
		if(y==2):
			o.setDaemon(True)
	for x in threads:
		x.start()
	for x in threads:
		x.join()
	for x in threads:
		print(x.isDaemon(),x.isAlive())