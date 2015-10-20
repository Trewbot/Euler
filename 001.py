import time
start = time.time()

sum = 0
for x in range(1, 1000):
	if x % 3 == 0 or x % 5 == 0:
		sum += x

print()
print(sum)
print("%.3f seconds" % (time.time() - start))
print()
