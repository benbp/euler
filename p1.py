multiples = []

mul3 = 3
mul5 = 5
total = 0

while mul5 < 1000:
	total += mul5
	mul5 += 5

while mul3 < 1000:
	if mul3 % 5 != 0:
		total += mul3
	mul3 += 3

print total
