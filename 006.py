import sys
import time

def sumOfSquares(thru):
	sum = 1
	for i in range(2,thru+1):
		sum += i**2
	return sum

def squareOfSums(thru):
	sum = 1
	for i in range(2,thru+1):
		sum += i
	return sum**2
	
def sumSqDiff(thru):
	return squareOfSums(thru) - sumOfSquares(thru)

thru = (len(sys.argv) > 1 and int(sys.argv[1])) or 100

print()
start = time.time()
print(sumSqDiff(thru))
print("%.3f seconds" % (time.time() - start))
print()