import sys
import time

def isPrime(n):
	if(n <= 2):
		return 1
	for j in range(2, n - 1):
		if n % j == 0:
			return 0
	return 1
	
def nthPrime(n):
	pn = 0
	i = 3
	while 1:
		if i % 5 == 0 and i > 5:
			i += 2
			continue
		if isPrime(i):
			pn += 1
		if pn == n - 1:
			return i
		i += 2

thru = (len(sys.argv) > 1 and int(sys.argv[1])) or 10001

print()
start = time.time()
print(nthPrime(thru))
print("%.3f seconds" % (time.time() - start))
print()