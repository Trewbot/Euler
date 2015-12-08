import sys
import time
import math
	
def sumOfDigitsOf2ExpN(n):
	exp = int(2 ** n)
	sum = 0
	for i in range(0,len(str(exp))):
		sum += int(str(exp)[i])
	return sum

n = (len(sys.argv) > 1 and int(sys.argv[1])) or 1e3

print()
start = time.time()
print(sumOfDigitsOf2ExpN(n))
print("%.3f seconds" % (time.time() - start))
print()