import sys
import time
import math

def multipleLoop(n, thru):
	for i in range(1, thru + 1):
		if(n % i > 0):
			return 0
	return 1

def isPrime(n):
	if(n <= 2):
		return 1
	for j in range(2, n - 1):
		if n % j == 0:
			return 0
	return 1
	
def findMultiple(thru):
	b = 1
	for i in range(1, thru + 1):
		if isPrime(i):
			b *= i
	a = thru*b
	while 1:
		if(multipleLoop(a, thru)):
			return a
		a += b

thru = (len(sys.argv) > 1 and int(sys.argv[1])) or 20

print()
start = time.time()
print(findMultiple(thru))
print("%.2f seconds" % (time.time() - start))
print()
