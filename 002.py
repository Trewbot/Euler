m = 1
n = 2
sum = 0
while n <= 4e6:
	if n % 2 == 0:
		sum += n
	o = n
	n = m + n
	m = o
print(sum)