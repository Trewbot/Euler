import sys
import time
import math

def isPerfectSquare(n):
	return math.sqrt(n) % 1 == 0

def findPythagoreanTripleProduct(sum):
	a = 1
	while a < sum:
		b = 1
		while b <= a:
			if not isPerfectSquare((a ** 2) + (b ** 2)):
				b += 1
				continue
			c = int(math.sqrt((a ** 2) + (b ** 2)))
			if a + b + c == sum:
				return str(a) + " * " + str(b) + " * " + str(c) + " = " + str(a * b * c)
			b += 1
		a += 1

sum = (len(sys.argv) > 1 and int(sys.argv[1])) or 1000

print()
start = time.time()
print(findPythagoreanTripleProduct(sum))
print("%.3f seconds" % (time.time() - start))
print()