import random

# Function to compute GCD (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Miller-Rabin Primality Test
def miller_rabin(n, k=5):  # Number of tests
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to generate a prime number with a bit length of 128 bits
def generate_prime(bits=128):
    while True:
        num = random.getrandbits(bits)
        if num % 2 == 0:
            num += 1  # Ensure the number is odd
        if miller_rabin(num):
            return num

# Function to generate RSA keys with 256-bit modulus (32 bytes)
def generate_rsa_keys():
    p = generate_prime(128)  # Generate a 128-bit prime number for p
    q = generate_prime(128)  # Generate a 128-bit prime number for q
    
    n = p * q  # Modulus n = p * q
    phi = (p - 1) * (q - 1)  # Euler's Totient function φ(n)
    
    e = 65537  # Public exponent (common choice)
    d = modinv(e, phi)  # Private exponent
    
    return (e, n), (d, n)

# Save the keys to files
def save_rsa_keys():
    public_key, private_key = generate_rsa_keys()

    with open("public.pem", "w") as pub_file:
        pub_file.write(f"{public_key[0]} {public_key[1]}")

    with open("private.pem", "w") as priv_file:
        priv_file.write(f"{private_key[0]} {private_key[1]}")

    print("Keys saved to 'public.pem' and 'private.pem'.")

# Call this function to generate and save keys
save_rsa_keys()
