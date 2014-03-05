seq = [1, 2]
total = 0

while seq[-1] <= 4000000:
	if seq[-1] % 2 == 0:
		total += seq[-1]
	seq.append(seq[-2]+seq[-1])

print total
