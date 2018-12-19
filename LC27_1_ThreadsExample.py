import threading as th
import time

def worker(num):
	#while True:
	#	print("1")
	time.sleep(1)
	print(th.currentThread().getName())
	print("Worker: %s" %num)
	
threads=[]
if __name__=="__main__":
	#t = th.Thread(target = worker)
	#t.setDaemon(True)#to make a daemon process
	#t.start()
	#t.join()#not returning control until the thread is done processing
	
	for i in range(5):
		t=th.Thread(target = worker, args=(i,),name="t"+str(i))
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