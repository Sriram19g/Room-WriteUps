import hashlib
import binascii

# Given hash parameters
salt = binascii.unhexlify("8bf3e3452b78544f8bee9400d6936d34")  # Convert hex to bytes
iterations = 50000
dk_len = 50  # Derived key length in bytes
expected_derived_key = "e531d398946137baea70ed6a680a54385ecff131309c0bd8f225f284406b7cbc8efc5dbef30bf1682619263444ea594cfb56"

# Wordlist path (update this to your actual wordlist file)
wordlist_path = "/usr/share/wordlists/rockyou.txt"

# Open the wordlist and test each password
with open(wordlist_path, "r", encoding="latin-1") as wordlist:
    for password in wordlist:
        password = password.strip().encode()  # Convert password to bytes

        # Compute PBKDF2-HMAC-SHA256
        derived_key = hashlib.pbkdf2_hmac('sha256', password, salt, iterations, dk_len)
        derived_key_hex = binascii.hexlify(derived_key).decode()

        # Check if the derived key matches
        if derived_key_hex == expected_derived_key:
            print(f"[+] Password Found: {password.decode()}")
            break
    else:
        print("[-] Password not found in wordlist.")

