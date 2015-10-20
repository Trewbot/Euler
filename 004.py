import sys
import time

def palindrome(num):
	return str(num)==str(num)[::-1]

def largestPalindrome(dig):
	min = 10 ** (dig - 1)
	max = (10 ** (dig)) - 1
	a = max
	top = (10 ** (dig)) + 1
	while a >= min:
		if top >= a * max:
			break
		b = max
		while b >= a:
			p = a * b
			if p > top and palindrome(p):
				top = p
			b -= 1
		a -= 1
	return top
dig = (len(sys.argv) > 1 and int(sys.argv[1])) or 3

print()
start = time.time()
print(largestPalindrome(dig))
print("%.3f seconds" % (time.time() - start))
print()