def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

n = int(input("n = "))
print(f"{n} is {'prime' if is_prime(n) else 'not prime'}.")
