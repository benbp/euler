"""
http://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# palindromic numbers
pnums = []

for i in range(100*100, (999*999)+1):
	if str(i)[::-1] == str(i):
		pnums.insert(0, i)

def find_palindrome():
	for pnum in pnums:
		n1 = 999.0
	
		while n1 > 99:
			if pnum % n1 == 0:
				if pnum / n1 > 99 and pnum / n1 < 1000:
					return pnum, n1, pnum/n1
			n1 -= 1

print find_palindrome()
