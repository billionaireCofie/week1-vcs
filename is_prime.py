import sys
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(sys.argv[1])
if is_prime(number):
    print(number, "is prime.")
else:
    print(number, "is not prime.")