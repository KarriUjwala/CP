def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def print_alternate_primes(n):
    primes = generate_primes(2 * n)  # Generate extra prime numbers
    for i in range(n):
        print(primes[i * 2], end=" ")

# Example 
n = int(input("Enter the value of N: "))
print_alternate_primes(n)
