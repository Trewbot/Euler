import sys
import time

def collatzSequence(n):
	seq = [n]
	while n > 1:
		if n % 2:
			n *= 3
			n += 1
			seq.append(int(n))
		else:
			n /= 2
			seq.append(int(n))
	return seq

	
def longestCollatzUnderN(n):
	length = 0
	max = 0
	for i in range(1,n):
		cs = len(collatzSequence(i))
		if cs > length:
			max = i
			length = cs
	return max
	
n = (len(sys.argv) > 1 and int(sys.argv[1])) or 1000000
	
print()
start = time.time()
c = longestCollatzUnderN(n)
print(c)
print("%.3f seconds" % (time.time() - start))
print()