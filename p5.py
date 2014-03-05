"""
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def analyze(num, div, divMax):
	result = False
	if num % div == 0:
		if div > 9:
			print div, num
		if div == divMax:
			result = True
		if not result:
			result = analyze(num, div+1, divMax)
	return result

def find_num(n, inc, low, high):
	while 1:
		if(analyze(n, low, high)):
			return n
		n += inc
	return 0

print find_num(149848560, 20, 3, 19)
