import time
n=0
horaInicio=time.time()
while n < 100000000:
	n=n+1
	# print(n)
print(time.time() - horaInicio)