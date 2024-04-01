def power_mod(a, b, m):
    result = 1
    a %= m  
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result

# Example
a, b, m = map(int, input("Enter three numbers a, b, and m separated by space: ").split())
result = power_mod(a, b, m)
print(f"(a^b % m) = {result}")
