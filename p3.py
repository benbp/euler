bignum = 600851475143
sqrNum = bignum**0.5

i = 3.0
factor = bignum

def is_prime(num):
	divisor = 3.0
	sqroot = num**0.5
	while divisor <= sqroot:
		if num % divisor == 0:
			return False
		divisor += 2
	return True

while factor > sqrNum:
	while bignum % i != 0:
		i+= 2
	factor = bignum / i
	i += 2

while not is_prime(factor):
	while bignum % i != 0:
		i += 2
	factor = bignum / i
	i += 2

print factor
