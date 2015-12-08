import sys
import time
import math
	
def latticePaths(n):
	return math.factorial(2 * n) / (math.factorial(n) ** 2)

n = (len(sys.argv) > 1 and int(sys.argv[1])) or 20

print()
start = time.time()
print(latticePaths(n))
print("%.3f seconds" % (time.time() - start))
print()