import sys
top = (len(sys.argv) > 1 and int(sys.argv[1])) or 4e6
m = 1
n = 2
sum = 0
while n <= top:
	if n % 2 == 0:
		sum += n
	o = n
	n = m + n
	m = o
print(sum)