import random
import time

def u(n):
	start = time.time()
	sum = 0.0
	percent = 0.0
	counter = 0
	step = n / 1000
	for i in range(n):
		sum += random.random()
		counter += 1
		if counter > step:
			print float(i) / n
			counter -= step
	print 'u =', sum / n
	print 'Running Time:', time.time()-start
