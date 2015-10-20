import sys
import time

num = (len(sys.argv) > 1 and int(sys.argv[1])) or 600851475143
def factors(n):
	factors = []
	d = 2
	while n > 1:
		while n % d == 0:
			factors.append(int(d))
			n /= d
		d += 1
		if d**2 > n:
			if n > 1: factors.append(int(n))
			break
	return factors

print()
start = time.time()
print(max(factors(num)))
print("%.3f seconds" % (time.time() - start))
print()