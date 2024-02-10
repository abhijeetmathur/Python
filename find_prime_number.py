def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

def prime_number(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes

prime_number = prime_number(20)
print("Prime numbers up to 20:", prime_number)
