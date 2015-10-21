import sys
import time
import math

def isPrime(n):
	if n == 1:
		return 0
	if n < 4:
		return 1
	for j in range(3, math.ceil(math.sqrt(n)) + 1):
		if n % j == 0:
			return 0
	return 1
	
def productToNthPrime(n):
	s = 5
	i = 5
	two = 1
	while i < n:
		if isPrime(i):
			s += i
		if two:
			i += 2
		else:
			i += 4
		two = not two
	return s

n = (len(sys.argv) > 1 and int(sys.argv[1])) or 2e6

print()
start = time.time()
print(productToNthPrime(n))
print("%.3f seconds" % (time.time() - start))
print()