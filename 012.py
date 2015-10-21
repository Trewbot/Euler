import sys
import time

def indexInList(list,val):
	try:
		return list.index(val)
	except ValueError:
		return -1

def divisors(n):
	a = 1
	divs = []
	while a < n and indexInList(divs,a) < 0:
		if n % a == 0:
			divs.append(a)
			if int(n / a) != a:
				divs.append(int(n / a))
		a += 1
	divs.sort()
	print(n)
	return divs

def firstTriangleNumWithNDivisors(n):
	a = 0
	sum = 0
	while 1:
		sum += a
		d = divisors(sum)
		if len(d) >= n:
			return sum
		a += 1

n = (len(sys.argv) > 1 and int(sys.argv[1])) or 500

print()
start = time.time()
print(firstTriangleNumWithNDivisors(n))
print("%.3f seconds" % (time.time() - start))
print()