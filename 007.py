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
	
def nthPrime(n):
	if n == 1:
		return 2
	if n == 2:
		return 3
	if n == 3:
		return 5
	pn = 2
	i = 5
	two = 1
	while 1:
		if isPrime(i):
			pn += 1
		if pn == n:
			return i
		if two:
			i += 2
		else:
			i += 4
		two = not two

thru = (len(sys.argv) > 1 and int(sys.argv[1])) or 10001

print()
start = time.time()
print(nthPrime(thru))
print("%.3f seconds" % (time.time() - start))
print()