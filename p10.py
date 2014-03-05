total = 2

def is_prime(num):
        divisor = 3.0
        sqroot = num**0.5
        while divisor <= sqroot:
                if num % divisor == 0:
                        return False
                divisor += 2
        return True

for i in range(3, 2000000, 2):
	if is_prime(i):
		total += i

print total
