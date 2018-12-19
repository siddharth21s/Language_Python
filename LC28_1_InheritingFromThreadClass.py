import threading

class subthread(threading.Thread):
	
	def run(self):
		print("Running")
		return
		
for i in range(5):
	t = subthread()
	t.start()