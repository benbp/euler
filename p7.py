i = 2
prime = 3

def is_prime(num):
        divisor = 3.0
        sqroot = num**0.5
        while divisor <= sqroot:
                if num % divisor == 0:
                        return False
                divisor += 2
        return True

while i < 10001:
	prime += 2
	if is_prime(prime):
		i += 1

print prime, i
